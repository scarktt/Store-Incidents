import json
from pathlib import Path
from store import Store
from incidents import Incidents


CURRENT_DIR_PATH = Path(__file__).parent.resolve()
FILE_NAME = 'incidents_data'


def _open_json(basepath: str, file_name: str) -> dict:
    with open(f"{basepath}/{file_name}.json", "r", encoding="utf-8") as data_json:
        data = json.load(data_json)
    return data


def start():
    incidents_data = _open_json(CURRENT_DIR_PATH, FILE_NAME)
    # Since incidents data is a list of dictionaries,
    # we can easily unpack it and create a list of Incidents objects.
    some_incidents = list(map(lambda incident: Incidents(**incident), incidents_data))
    
    some_store = Store(some_incidents)
    incident_status = some_store.incident_status('01/10/2022 00:00:00', '04/06/2022 12:59:59')
    print(json.dumps(incident_status, indent=4))


if __name__ == '__main__':
    start()
    