import pathlib
import sqlite3
import json
from typing import Generator

import inflection
import ndjson


class LocalFHIRDatabase:
    def __init__(self, db_name):  # , db_name=pathlib.Path('.g3t') / 'local.db'):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.table_created = {}  # Flag to track if the table has been created

    def connect(self) -> sqlite3.Cursor:
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def create_table(
            self,
            name='resources',
            ddl='''
                    CREATE TABLE __NAME__ (
                        key TEXT PRIMARY KEY,
                        resource_type TEXT,
                        resource JSON
                    )
                '''):
        self.connect()
        # Check if the table exists before creating it
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}'")
        table_exists = self.cursor.fetchone()

        if not table_exists:
            ddl = ddl.replace('__NAME__', name)
            self.cursor.execute(ddl)
            self.table_created[name] = True

    def count(self, table_name='resources'):
        self.connect()
        self.cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = self.cursor.fetchone()[0]
        return count

    def insert_data(self, id_, resource_type, resource, table_name='resources'):
        """Insert data into the database."""
        if table_name not in self.table_created:
            self.create_table(table_name)  # Lazily create the table if not already created

        composite_key = f"{resource_type}/{id_}"
        self.cursor.execute(f'''
            INSERT INTO {table_name} (key, resource_type, resource)
            VALUES (?, ?, ?)
        ''', (composite_key, resource_type, json.dumps(resource)))
        # print(f"Inserted {composite_key} into the database")

    def insert_data_from_dict(self, resource, table_name='resources'):
        """Insert data into the database from a dictionary."""
        if 'id' not in resource or ('resource_type' not in resource and 'resourceType' not in resource):
            raise ValueError(f"Resource dictionary must contain 'id' and 'resource_type' keys {resource}")
        self.insert_data(
            resource['id'],
            resource.get('resource_type', resource.get('resourceType')),
            resource,
            table_name
        )

    def bulk_insert_data(self, resources, table_name='resources') -> int:
        """Bulk insert data into the database."""

        if table_name not in self.table_created:
            self.create_table(table_name)  # Lazily create the table if not already created

        def _prepare(resource):
            resource_type = resource.get('resource_type', resource.get('resourceType'))
            id_ = resource['id']
            composite_key = f"{resource_type}/{id_}"
            return (
                composite_key,
                resource_type,
                json.dumps(resource)
            )

        def _iterate(_resources):
            for _ in _resources:
                yield _prepare(_)

        try:
            self.connect()
            sql = f'''
                INSERT INTO {table_name} (key, resource_type, resource)
                VALUES (?, ?, ?)
            '''
            new_cursor = self.cursor.executemany(sql, _iterate(_resources=resources))
            print(f"Inserted {new_cursor.rowcount} rows into the database {sql}")

        finally:
            self.connection.commit()
            # self.disconnect()

        return new_cursor.rowcount

    def load_from_ndjson_file(self, file_path, table_name='resources'):
        """Load the NDJSON file into the database."""

        if table_name not in self.table_created:
            self.create_table(table_name)  # Lazily create the table if not already created

        with open(file_path, 'r') as file:
            reader = ndjson.reader(file)
            self.bulk_insert_data(reader)

    def load_ndjson_from_dir(self, path: str = 'META', pattern: str = '*.ndjson'):
        """Load all the NDJSON files in the directory into the database."""
        for file_path in pathlib.Path(path).glob(pattern):
            self.load_from_ndjson_file(file_path)

    def patient_everything(self, patient_id) -> Generator[dict, None, None]:
        """Return all the resources for a patient."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM resources WHERE json_extract(resource, '$.subject.reference') = ?",
                       (f"Patient/{patient_id}",))

        for _ in cursor.fetchall():
            key, resource_type, resource = _
            yield json.loads(resource)

    def patient(self, patient_id) -> dict:
        """Return the patient resource."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM resources WHERE json_extract(resource, '$.id') = ?", (patient_id,))
        key, resource_type, resource = cursor.fetchone()
        return json.loads(resource)

    def flattened_procedure(self) -> Generator[dict, None, None]:
        """Return all the procedures with everything resolved"""
        loaded_db = self
        connection = sqlite3.connect(loaded_db.db_name)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM resources where resource_type = ?", ("Procedure",))

        for _ in cursor.fetchall():
            key, resource_type, procedure = _
            procedure = json.loads(procedure)
            # simplify the identifier
            procedure['identifier'] = procedure['identifier'][0]['value']
            # simplify the code
            procedure['code'] = procedure['code']['coding'][0]['display']
            # simplify the reason
            procedure['reason'] = procedure['reason'][0]['reference']['reference']
            # simplify the occurrenceAge
            procedure['occurrenceAge'] = procedure['occurrenceAge']['value']
            # simplify the subject
            subject = procedure['subject']['reference']
            procedure['subject'] = subject

            if subject.startswith('Patient/'):
                _, patient_id = subject.split('/')
                resources = [_ for _ in loaded_db.patient_everything(patient_id)]
                resources.append(loaded_db.patient(patient_id))
                for resource in resources:

                    if resource['resourceType'] == 'Patient':
                        procedure['patient'] = resource['identifier'][0]['value']
                        continue

                    if resource['resourceType'] == 'Condition' and f"Condition/{resource['id']}" == procedure['reason']:
                        procedure['reason'] = resource['code']['text']
                        continue

                    if resource['resourceType'] == 'Observation':
                        # must be focus
                        if f"Procedure/{procedure['id']}" not in [_['reference'] for _ in resource['focus']]:
                            continue

                        # TODO - pick first coding, h2 allow user to specify preferred coding
                        code = resource['code']['coding'][0]['code']

                        if 'valueQuantity' in resource:
                            value = resource['valueQuantity']['value']
                        elif 'valueCodeableConcept' in resource:
                            value = resource['valueCodeableConcept']['text']
                        elif 'valueInteger' in resource:
                            value = resource['valueInteger']
                        elif 'valueString' in resource:
                            value = resource['valueString']
                        else:
                            print(f"no value for {resource['id']}")
                            value = None

                        assert value is not None, f"no value for {resource['id']}"
                        procedure[code] = value

                        continue

                    # skip these
                    if resource['resourceType'] in ['Specimen', 'Procedure', 'ResearchSubject']:
                        continue

                    # default, add entire resource as an item of the list
                    resource_type = inflection.underscore(resource['resourceType'])
                    if resource_type not in procedure:
                        procedure[resource_type] = []
                    procedure[resource_type].append(resource)

            yield procedure

        connection.close()
