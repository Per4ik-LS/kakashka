import json
from random import random

from flask_restful import reqparse, abort, Api, Resource

import requests


def main_job() -> None:
    test_add_job()


BASE_URL = 'http://localhost:5000/api'


def test_all_jobs() -> None:
    response = requests.get(f'{BASE_URL}/jobs')
    data = response.json()
    print(json.dumps(data, indent=4))


def test_all_job_1() -> None:
    response = requests.get(f'{BASE_URL}/jobs/1')
    data = response.json()
    print(json.dumps(data, indent=4))


def test_all_job_999() -> None:
    response = requests.get(f'{BASE_URL}/jobs/999')
    data = response.json()
    print(json.dumps(data, indent=4))


def test_all_job_qwerty() -> None:
    response = requests.get(f'{BASE_URL}/jobs/qwerty')
    print(response.status_code)


def test_add_job() -> None:
    response = requests.post(f'{BASE_URL}/jobs', json={
        'id': random.randint(1000, 10000),
        'job': 'installation of radiation protection',
        'team_leader': 1,
        'work_size': 45,
        'collaborators': '6, 4, 7',
        'is_finished': False,
    })
    data = response.json()
    print(json.dumps(data, indent=4))
    test_all_jobs()


def test_add_job_already_exists() -> None:
    response = requests.post(f'{BASE_URL}/jobs', json={
        'id': 1,
        'job': 'installation of radiation protection',
        'team_leader': 1,
        'work_size': 45,
        'collaborators': '6, 4, 7',
        'is_finished': False,
    })
    data = response.json()
    print(json.dumps(data, indent=4))
    test_all_jobs()