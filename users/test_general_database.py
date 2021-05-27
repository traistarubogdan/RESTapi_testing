"""
Positive and negative tests for global database
"""

import pytest
import logging

logging.basicConfig(filename='../Logs/logs.txt', level=logging.INFO)
logger = logging.getLogger()


@pytest.mark.bogdan
@pytest.mark.positive_testing
@pytest.mark.global_database_tests
def test_get_request(get_request_global):
    response = get_request_global()
    assert response.status_code == 200


@pytest.mark.positive_testing
@pytest.mark.global_database_tests
def test_post_request(post_request):

    response, expected_data = post_request()
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data']['name'] == expected_data['name']
    assert response['data']['email'] == expected_data['email']
    assert response['data']['gender'] == expected_data['gender']
    assert response['data']['status'] == expected_data['status']


@pytest.mark.positive_testing
@pytest.mark.global_database_tests
def test_delete_request(delete_request):

    response = delete_request()
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data'] == None


@pytest.mark.negative_testing
@pytest.mark.global_database_tests
def test_get_request_invalid_url(get_request_global):

    response = get_request_global(alterate_string='test')
    assert response.status_code == 404


@pytest.mark.negative_testing
@pytest.mark.global_database_tests
def test_post_request_invalid_email(post_request):

    response, expected_data = post_request(alterate_email=True)
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data'][0]['field'] == 'email'
    assert response['data'][0]['message'] == 'is invalid'


@pytest.mark.negative_testing
@pytest.mark.global_database_tests
def test_post_request_invalid_gender(post_request):

    response, expected_data = post_request(alterate_gender=True)
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data'][0]['field'] == 'gender'
    assert response['data'][0]['message'] == 'can be Male or Female'


@pytest.mark.negative_testing
@pytest.mark.global_database_tests
def test_post_request_invalid_status(post_request):

    response, expected_data = post_request(alterate_status=True)
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data'][0]['field'] == 'status'
    assert response['data'][0]['message'] == 'can be Active or Inactive'


@pytest.mark.negative_testing
@pytest.mark.global_database_tests
def test_delete_request_invalid_id(delete_request):

    response = delete_request(id="test")
    assert response.status_code == 200

    response = response.json()
    logger.info(response)
    assert response['data']['message'] == "Resource not found"
