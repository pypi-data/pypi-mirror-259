import pathlib
import sqlite3
import json
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

        if table_name not in self.table_created:
            self.create_table(table_name)  # Lazily create the table if not already created

        composite_key = f"{resource_type}/{id_}"
        self.cursor.execute(f'''
            INSERT INTO {table_name} (key, resource_type, resource)
            VALUES (?, ?, ?)
        ''', (composite_key, resource_type, json.dumps(resource)))
        # print(f"Inserted {composite_key} into the database")

    def insert_data_from_dict(self, resource, table_name='resources'):
        if 'id' not in resource or ('resource_type' not in resource and 'resourceType' not in resource):
            raise ValueError(f"Resource dictionary must contain 'id' and 'resource_type' keys {resource}")
        self.insert_data(
            resource['id'],
            resource.get('resource_type', resource.get('resourceType')),
            resource,
            table_name
        )

    def bulk_insert_data(self, resources, table_name='resources') -> int:

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

        if table_name not in self.table_created:
            self.create_table(table_name)  # Lazily create the table if not already created

        with open(file_path, 'r') as file:
            reader = ndjson.reader(file)
            self.bulk_insert_data(reader)

    def load_ndjson_from_dir(self, path: str = 'META', pattern: str = '*.ndjson'):
        for file_path in pathlib.Path(path).glob(pattern):
            self.load_from_ndjson_file(file_path)

    def load_ndjson_from_dir(self, path: str = 'META', pattern: str = '*.ndjson'):
        for file_path in pathlib.Path(path).glob(pattern):
            self.load_from_ndjson_file(file_path)



#
# # Example usage:
# fhir_db = LocalFHIRDatabase()
#
# # Assuming 'data.ndjson' is a newline-delimited JSON file with resource data
# fhir_db.load_from_ndjson_file('data.ndjson')
