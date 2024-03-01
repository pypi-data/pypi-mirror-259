import json
from mixin_sdk import auth
from mixin_sdk.request import request


def read_user(user_id, client_id, session_id, private_key ):
    uri = '/users/' + user_id
    access_token = auth.generate_authentication_token('GET', uri, '', client_id, session_id, private_key)
    custom_headers = {"Authorization": "Bearer " + access_token}
    user_info = request(uri=uri, method="GET", payload=None, custom_headers=custom_headers)
    return user_info


def read_users(user_id_list, client_id, session_id, private_key):
    uri = '/users/fetch'
    body = json.dumps(user_id_list)
    access_token = auth.generate_authentication_token('POST', uri, body, client_id, session_id, private_key)
    custom_headers = {"Authorization": "Bearer " + access_token}
    user_info = request(uri=uri, method="POST", payload=user_id_list, custom_headers=custom_headers)
    return user_info

def search_user(mixin_id, client_id, session_id, private_key):
    uri = '/search/' + mixin_id
    access_token = auth.generate_authentication_token('GET', uri, '', client_id, session_id, private_key)
    custom_headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    user_info = request(uri=uri, method="GET", custom_headers=custom_headers)
    return user_info
