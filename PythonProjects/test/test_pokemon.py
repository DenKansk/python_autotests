import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd314ded3894aa27a3978c472bcf3d5ac'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '33412'
TRAINER_NAME = 'VenoM'

def test_status_code ():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER)
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('id', TRAINER_ID), ('trainer_name', TRAINER_NAME)])
def test_part_of_response (key, value):
    response_params = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id' : TRAINER_ID})
    assert response_params.json()["data"][0][key] == value