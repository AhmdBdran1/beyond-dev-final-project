import json
import os
import random
from datetime import datetime, timedelta

from jira import JIRA


def generate_random_object_id():
    random_id = ''.join(random.choice('0123456789abcdef') for i in range(24))
    return random_id


def create_jira_issue(summary, description):
    # Create JIRA issue with relevant information
    private_config = read_private_config()
    temp_token = private_config['token']
    token = temp_token[4:]
    email = private_config['email']
    jira_url = private_config['jira_url']
    project_token = private_config['project_token']

    auth_jira = JIRA(
        basic_auth=(email, token),
        options={'server': jira_url}
    )
    issue_dict = {
        'project': {'key': project_token},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Bug'},
    }

    # Create the issue
    auth_jira.create_issue(fields=issue_dict)


def read_config():  # open the config file for read
    script_directory = os.path.dirname(os.path.realpath(__file__))
    absolute_path = os.path.join(script_directory, "config.json")
    with open(absolute_path, 'r') as f:
        config = json.load(f)
    return config


def read_private_config():  # open the config file for read
    script_directory = os.path.dirname(os.path.realpath(__file__))
    absolute_path = os.path.join(script_directory, "private_config.json")
    with open(absolute_path, 'r') as f:
        config = json.load(f)
    return config


def read_from_secret_file():
    script_directory = os.path.dirname(os.path.realpath(__file__))
    absolute_path = os.path.join(script_directory, "private_config.json")
    with open(absolute_path, 'r') as f:
        config = json.load(f)
    return config


# Function to generate random latitude and longitude within a specified range
def generate_random_coordinates():
    latitude = round(random.uniform(-90, 90), 4)
    longitude = round(random.uniform(-180, 180), 4)
    return latitude, longitude


# Function to generate a random datetime within a specified range
def generate_random_datetime():
    start_date = datetime.now() - timedelta(days=365)  # One year ago
    end_date = datetime.now()
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.isoformat()


# Function to generate random temperature and humidity values
def generate_random_temperature_and_humidity():
    temperature = round(random.uniform(-20, 40), 1)
    humidity = random.randint(0, 100)
    return temperature, humidity


# function to get the data when need to create as new observation
def get_observation_data_as_json(location_id, owner_id):
    return {
        "comment": "",
        "difficulty": 0,
        "id": generate_random_object_id(),
        "location": location_id,
        "observing_setup": {
            "id": "eyes_observation"
        },
        "owner": owner_id,
        "rating": 0,
        "target": {
            "culturalNames": [],
            "interest": 4.3176,
            "match": "NAME Alpheratz",
            "model": "star",
            "model_data": {
                "Bmag": 1.95,
                "Imag": 2.19,
                "Rmag": 2.09,
                "Umag": 1.48,
                "Vmag": 2.06,
                "de": 29.090431118,
                "plx": 33.62,
                "pm_de": -163.44,
                "pm_ra": 137.46,
                "ra": 2.096916186,
                "rv": -10.1,
                "spect_t": "B8IV-VHgMn"
            },
            "names": [
                "NAME Alpheratz",
                "* alf And",
                "* del Peg",
                "* 21 And",
                "V* alf And",
                "HD 358",
                "HR 15",
                "SAO 73765",
                "HIP 677",
                "TYC 1735-3180-1",
                "BD+28 4",
                "FK5 1",
                "HGAM 2",
                "YPAC 1",
                "** JNN 1A",
                "PLX 12",
                "SBC9 4",
                "ADS 94 A",
                "GCRV 62",
                "ROT 58",
                "SBC7 4",
                "UBV 52",
                "Renson 50",
                "** MKT 11",
                "WEB 113",
                "GC 127",
                "HIC 677",
                "NLTT 346",
                "SKY# 244",
                "TD1 31",
                "** H 532A",
                "AG+28 11",
                "CSI+28 4 1",
                "N30 16",
                "UBV M 7157",
                "IRC +30004",
                "JP11 345",
                "LTT 10039",
                "PMC 90-93 1",
                "PPM 89441",
                "SRS 30001",
                "ALS 16723",
                "ASCC 647497",
                "EUVE J0008+29.0",
                "UCAC3 239-808",
                "LSPM J0008+2905",
                "CCDM J00083+2905A",
                "GEN# +1.00000358",
                "IDS 00032+2832 A",
                "WDS J00084+2905Aa,Ab",
                "IRAS 00057+2848",
                "WDS J00084+2905A",
                "GSC 01735-03180",
                "uvby98 100000358",
                "USNO-B1.0 1190-00002295",
                "AKARI-IRC-V1 J0008233+290524",
                "2MASS J00082326+2905253"
            ],
            "short_name": "Ahmd",
            "types": ["a2*", "Ro*", "V*", "*"]
        },
        "time": 60377.69831566018,
        "updated_at": "2024-03-08T16:47:00.969000+00:00"
    }


# function to get the data when need to create as new observation
def get_observation_data_as_json_for_updating(observation_id, location_id, owner_id):
    return {
        "comment": "updated",
        "difficulty": 0,
        "id": observation_id,
        "location": location_id,
        "observing_setup": {
            "id": "eyes_observation"
        },
        "owner": owner_id,
        "rating": 0,
        "target": {
            "culturalNames": [],
            "interest": 4.3176,
            "match": "NAME Alpheratz",
            "model": "star",
            "model_data": {
                "Bmag": 1.95,
                "Imag": 2.19,
                "Rmag": 2.09,
                "Umag": 1.48,
                "Vmag": 2.06,
                "de": 29.090431118,
                "plx": 33.62,
                "pm_de": -163.44,
                "pm_ra": 137.46,
                "ra": 2.096916186,
                "rv": -10.1,
                "spect_t": "B8IV-VHgMn"
            },
            "names": [
                "NAME Alpheratz",
                "* alf And",
                "* del Peg",
                "* 21 And",
                "V* alf And",
                "HD 358",
                "HR 15",
                "SAO 73765",
                "HIP 677",
                "TYC 1735-3180-1",
                "BD+28 4",
                "FK5 1",
                "HGAM 2",
                "YPAC 1",
                "** JNN 1A",
                "PLX 12",
                "SBC9 4",
                "ADS 94 A",
                "GCRV 62",
                "ROT 58",
                "SBC7 4",
                "UBV 52",
                "Renson 50",
                "** MKT 11",
                "WEB 113",
                "GC 127",
                "HIC 677",
                "NLTT 346",
                "SKY# 244",
                "TD1 31",
                "** H 532A",
                "AG+28 11",
                "CSI+28 4 1",
                "N30 16",
                "UBV M 7157",
                "IRC +30004",
                "JP11 345",
                "LTT 10039",
                "PMC 90-93 1",
                "PPM 89441",
                "SRS 30001",
                "ALS 16723",
                "ASCC 647497",
                "EUVE J0008+29.0",
                "UCAC3 239-808",
                "LSPM J0008+2905",
                "CCDM J00083+2905A",
                "GEN# +1.00000358",
                "IDS 00032+2832 A",
                "WDS J00084+2905Aa,Ab",
                "IRAS 00057+2848",
                "WDS J00084+2905A",
                "GSC 01735-03180",
                "uvby98 100000358",
                "USNO-B1.0 1190-00002295",
                "AKARI-IRC-V1 J0008233+290524",
                "2MASS J00082326+2905253"
            ],
            "short_name": "updated",
            "types": ["a2*", "Ro*", "V*", "*"]
        },
        "time": 60377.69831566018,
        "updated_at": "2024-03-08T16:47:00.969000+00:00"
    }
