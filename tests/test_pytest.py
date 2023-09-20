"""
Pytest option for writing tests for the events app/endpoints.

Ensure you have pytest installed and imported before running these tests:
`pip install pytest`
`import pytest`

To run the tests, execute the following line of code:
`pytest`

"""
# tests/test_api.py

import requests

def test_get_user_groups():
    # Replace 'http://localhost:5000' with the actual URL of your API
    base_url = 'http://127.0.0.1:5000'
    user_id = 1
    endpoint = f'{base_url}/api/{user_id}/groups'

    response = requests.get(endpoint)

    assert response.status_code == 200
    data = response.json()
    assert 'user_id' in data
    assert 'groups' in data
