import os
import pathlib
import sqlite3
import json

import inflection
import pytest
from fhir.resources.patient import Patient

from g3t_etl.util.local_fhir_db import LocalFHIRDatabase


@pytest.fixture
def db_name(tmp_path):
    path = 'tests/fixtures/test_example.db'
    return path


@pytest.fixture
def db(db_name):
    if os.path.exists(db_name):
        os.remove(db_name)
    yield LocalFHIRDatabase(db_name=db_name)
    # os.remove(db_name)


@pytest.fixture
def file_path():
    return 'tests/fixtures/sample_fhir/Patient.ndjson'


@pytest.fixture
def patient_id():
    return "c377f672-45d3-5075-b23a-3a515565b4a8"


@pytest.fixture
def ndjson_dir():
    return 'tests/fixtures/sample_dataset-FHIR/dummy_data_30pid'


@pytest.fixture
def identifier_value():
    return "123"


def test_create_table(db):
    db.create_table()

    # Check if the table has been created in the database
    connection = sqlite3.connect(db.db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='resources'")
    table_exists = cursor.fetchone()
    connection.close()

    assert table_exists is not None, "Table 'resources' not created."


def test_insert_data(db):
    db.create_table()
    db.connect()
    data = {'id': '1', 'resource_type': 'Patient', 'key': 'value1', 'number': 42}
    db.insert_data_from_dict(data)
    db.connection.commit()

    # Check if the data has been inserted into the database
    connection = sqlite3.connect(db.db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM resources WHERE key=?", ('Patient/1',))
    result = cursor.fetchone()
    connection.close()

    assert result is not None, "Data not inserted into the database."
    assert result[0] == 'Patient/1', "Incorrect key value."
    assert result[1] == 'Patient', "Incorrect resource_type value."
    assert json.loads(result[2]) == data, "Incorrect resource value."


def test_load_from_ndjson_file(db, file_path):
    db.load_from_ndjson_file(file_path)

    # Check if the data from the NDJSON file has been inserted into the database
    connection = sqlite3.connect(db.db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM resources")
    count = cursor.fetchone()[0]
    connection.close()

    assert count > 0, "No data loaded from NDJSON file."


def test_load_json_query(db, file_path, patient_id, identifier_value):
    db.load_from_ndjson_file(file_path)

    # Check if the data from the NDJSON file has been inserted into the database
    connection = sqlite3.connect(db.db_name)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM resources WHERE json_extract(resource, '$.id') = ?", (patient_id,))
    key, resource_type, resource = cursor.fetchone()
    assert key == f"Patient/{patient_id}", key
    assert resource_type == 'Patient', resource_type
    assert resource is not None, resource
    resource = json.loads(resource)
    assert resource['id'] == patient_id, resource

    cursor.execute("SELECT * FROM resources WHERE json_extract(resource, '$.identifier[0].value') = ?",
                   (identifier_value,))
    key, resource_type, resource = cursor.fetchone()
    assert resource_type == 'Patient', resource_type
    assert resource is not None, resource
    resource = json.loads(resource)
    assert resource['identifier'][0]['value'] == identifier_value, resource

    connection.close()


def test_loaded_data_valid(db, file_path):
    db.load_from_ndjson_file(file_path)

    # Check if the data from the NDJSON file has been inserted into the database
    connection = sqlite3.connect(db.db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT resource FROM resources")
    for _tuple in cursor.fetchall():
        resource = _tuple[0]
        Patient(**json.loads(resource))  # Raises an exception if the resource is not valid
    connection.close()


@pytest.fixture
def loaded_db(db, ndjson_dir):
    db.load_ndjson_from_dir(path=ndjson_dir)
    return db


@pytest.fixture
def expected_count():
    return 7457


@pytest.fixture
def patient_expected_resource_count():
    return 185


@pytest.fixture
def procedure_expected_resource_count():
    return 160


def test_load_from_dir(loaded_db, expected_count):
    """Check if the data from the NDJSON files has been inserted into the database"""
    connection = sqlite3.connect(loaded_db.db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM resources")
    count = cursor.fetchone()[0]
    connection.close()

    assert count == expected_count, f"Incomplete data loaded from NDJSON file. resource count: {count}"


def get_patient_everything(loaded_db, patient_id):
    connection = sqlite3.connect(loaded_db.db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM resources WHERE json_extract(resource, '$.subject.reference') = ?", (f"Patient/{patient_id}",))

    for _ in cursor.fetchall():
        key, resource_type, resource = _
        yield json.loads(resource)


def get_patient(loaded_db, patient_id):
    connection = sqlite3.connect(loaded_db.db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM resources WHERE json_extract(resource, '$.id') = ?", (patient_id,))
    key, resource_type, resource = cursor.fetchone()
    return json.loads(resource)


def test_patient_everything(loaded_db, patient_id, patient_expected_resource_count):
    """Check if the data from the NDJSON files has been inserted into the database"""

    resources = []
    c = 0

    for _ in get_patient_everything(loaded_db, patient_id):
        resources.append(_)
        c += 1
    assert c == patient_expected_resource_count, f"Expected {patient_expected_resource_count}, got {c}"

    patient = get_patient(loaded_db, patient_id)

    assert patient_id == patient['id'], f"Expected {patient_id}, got {patient['id']}"


def procedure_everything(loaded_db):
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
            resources = [_ for _ in get_patient_everything(loaded_db, patient_id)]
            resources.append(get_patient(loaded_db, patient_id))
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


def test_procedure_everything(loaded_db, procedure_expected_resource_count):
    """Check if the data from the NDJSON files has been inserted into the database"""

    c = loaded_db.bulk_insert_data(procedure_everything(loaded_db), table_name="procedure_everything")
    assert c == procedure_expected_resource_count, f"Expected {procedure_expected_resource_count}, got {c}"
    print(loaded_db.db_name)
    loaded_db.disconnect()
    assert loaded_db.count() > 0, "No data loaded from NDJSON file."
    assert loaded_db.count(table_name="procedure_everything") > 0, "No data loaded into procedure_everything."
    (resource, ) = loaded_db.connection.cursor().execute("SELECT resource FROM procedure_everything").fetchone()
    assert resource is not None, "No data loaded into procedure_everything."
    resource = json.loads(resource)
    assert 'id' in resource, "No id in resource"
    assert 'code' in resource, "No code in resource"
    assert 'gleason' in resource.keys(), "No gleason in resource"
