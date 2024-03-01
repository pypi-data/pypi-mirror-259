import jwt
import uuid
from hashlib import sha256
import datetime
from mixin_sdk.request import request


def generate_authentication_token(method, uri, body, client_id, session_id, private_key):
    iat = datetime.datetime.utcnow()
    exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=500)
    jti = str(uuid.uuid4())
    sig = sha256((method + uri + body).encode("UTF-8")).hexdigest()
    encoded = jwt.encode({"uid": client_id, "sid": session_id, "iat": iat, "exp": exp, "jti": jti, "sig": sig}, private_key, "RS512")
    return encoded.decode("UTF-8")


def get_access_token(code, client_id, secret):
    uri = "/oauth/token"
    payload = {"code": code, "client_id": client_id, "client_secret": secret}
    token_rsp = request(uri=uri, method="POST", payload=payload)
    if token_rsp:
        return token_rsp["data"]["scope"], token_rsp["data"]["access_token"]
    else:
        return None


def user_me(access_token):
    uri = "/me"
    custom_headers = {"Authorization": "Bearer "+access_token}
    user_me = request(uri=uri, method="GET", custom_headers=custom_headers)
    if user_me:
        return user_me
    else:
        return None




