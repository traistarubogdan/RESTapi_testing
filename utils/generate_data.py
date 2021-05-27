import random
import string

def generate_random_name():
    return ''.join(random.choices(string.ascii_lowercase, k=10))

def generate_random_email(alterate = False):
    if alterate == True:
        return ''.join(random.choices(string.ascii_lowercase, k=10))

    return ''.join(random.choices(string.ascii_lowercase, k=10)) + '@test.com'

def choose_random_gender(alterate = False):
    if alterate == True:
        return 'Test'

    return random.choice(['Male', 'Female'])

def choose_random_status(alterate = False):
    if alterate == True:
        return 'Test'

    return random.choice(['Active', 'Inactive'])


def generate_random_data(alterate_email=False, alterate_gender=False, alterate_status=False):
    return {'name' : generate_random_name(), 'email' : generate_random_email(alterate=alterate_email),
            'gender' : choose_random_gender(alterate=alterate_gender),
            'status' : choose_random_status(alterate=alterate_status)}