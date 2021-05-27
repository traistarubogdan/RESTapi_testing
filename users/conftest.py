import pytest
import random
import requests
import logging

from utils.generate_data import *

logging.basicConfig(filename='../Logs/logs.txt', level=logging.INFO)
logger = logging.getLogger()

token = 'eeb59586cc7c48255a6771a35b50f7f44792a2e621ff5021dca7f64ab47ab042'
header = {'Authorization': 'Bearer ' + token}


@pytest.fixture()
def url():
    """
    This fixture is used to return the URL
    :return: str
    """

    url = "https://gorest.co.in/public-api/users"
    return url


@pytest.fixture(name='user_id')
def get_random_user_id(url):
    """
    This fixture is used to pick a random user from existing users in database
    :param url: str
    :return: str
    """

    return str(random.choice(requests.get(url).json()['data'])['id'])


@pytest.fixture()
def get_request_global(url):
    """
    This fixture is used to call GET endpoint on global database
    :param url: str
    :return: json
    """
    def get_request_global_subfixture(alterate_string=""):
        logger.info('Call GET request')
        get_response = requests.get(url + alterate_string)
        logger.info('GET Response Status Code: ' + str(get_response.status_code))
        return get_response

    return get_request_global_subfixture


@pytest.fixture()
def post_request(url):
    """
    This fixture is used to call POST endpoint on global database
    :param url: str
    :return: json, dict
    """
    def post_request_subfixture(alterate_email=False, alterate_gender=False, alterate_status=False):
        random_data = generate_random_data(alterate_email=alterate_email,
                                           alterate_gender=alterate_gender, alterate_status=alterate_status)
        logger.info('Call POST request')
        post_response= requests.post(url, headers=header, data=random_data)
        logger.info('POST Response Status Code: ' + str(post_response.status_code))

        return post_response, random_data

    return post_request_subfixture


@pytest.fixture()
def get_request_user(url, user_id):
    """
    This fixture is used to call GET endpoint on a specific user
    :param url: str
    :param user_id: str
    :return: json
    """
    def get_request_user_subfixture(alterate_user_id=""):
        logger.info('Call GET request for a specific user')
        get_response = requests.get(url + "/" + user_id + alterate_user_id)
        logger.info('GET Response Status Code: ' + str(get_response.status_code))

        return get_response

    return get_request_user_subfixture


@pytest.fixture()
def put_request(url, user_id):
    """
    This fixture is used to call PUT endpoint on a specific user
    :param url: str
    :param user_id: str
    :return: json, dict
    """

    def put_request_subfixture(alterate_email=False, alterate_gender=False, alterate_status=False):
        random_data = generate_random_data(alterate_email=alterate_email,
                                           alterate_gender=alterate_gender, alterate_status=alterate_status)
        logger.info('Call PUT request')
        put_response= requests.put(url + "/" + user_id, headers=header, data=random_data)
        logger.info('PUT Response Status Code: ' + str(put_response.status_code))

        return put_response, random_data

    return put_request_subfixture


@pytest.fixture()
def delete_request(url, user_id):
    """
    This fixture is used to call DELETE endpoint on a specific user
    :param url: str
    :param user_id: str
    :return: json
    """
    def delete_request_subfixture(id=user_id):
        logger.info('Call DELETE request for a specific user')
        delete_response = requests.delete(url + "/" + id, headers=header)
        logger.info('DELETE Response Status Code: ' + str(delete_response.status_code))
        logger.info('Call GET request for a deleted user')
        get_response = requests.get(url + '/' + id)
        logger.info('GET Response Status Code: ' + str(get_response.status_code))
        assert get_response.json()['data']['message'] == "Resource not found"
        return delete_response

    return delete_request_subfixture
