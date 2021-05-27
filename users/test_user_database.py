"""
Positive and negative tests for a specific user
"""

import pytest
import logging

logging.basicConfig(filename='../Logs/logs.txt', level=logging.INFO)
logger = logging.getLogger()

@pytest.mark.positive_testing
@pytest.mark.user_database_tests
def test_get_request_user(get_request_user, user_id):

    response = get_request_user()
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data']['id'] == int(user_id)


@pytest.mark.positive_testing
@pytest.mark.user_database_tests
def test_put_request(put_request):

    response, expected_data = put_request()
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data']['name'] == expected_data['name']
    assert response['data']['email'] == expected_data['email']
    assert response['data']['gender'] == expected_data['gender']
    assert response['data']['status'] == expected_data['status']


@pytest.mark.negative_testing
@pytest.mark.user_database_tests
def test_get_request_user_invalid_user_id(get_request_user):

    response = get_request_user(alterate_user_id="000000")
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data']['message'] == 'Resource not found'


@pytest.mark.negative_testing
@pytest.mark.user_database_tests
def test_put_request_invalid_email(put_request):

    response, expected_data = put_request(alterate_email=True)
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data']['email'] == expected_data['email']


@pytest.mark.negative_testing
@pytest.mark.user_database_tests
def test_put_request_invalid_gender(put_request):

    response, expected_data = put_request(alterate_gender=True)
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data'][0]['field'] == 'gender'
    assert response['data'][0]['message'] == 'can be Male or Female'


@pytest.mark.negative_testing
@pytest.mark.user_database_tests
def test_put_request_invalid_status(put_request):

    response, expected_data = put_request(alterate_status=True)
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data'][0]['field'] == 'status'
    assert response['data'][0]['message'] == 'can be Active or Inactive'
