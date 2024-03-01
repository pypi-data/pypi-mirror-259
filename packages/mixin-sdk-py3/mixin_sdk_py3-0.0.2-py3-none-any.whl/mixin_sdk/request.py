import requests
from mixin_sdk import globalval


def request(uri=None, method="GET", payload=None, custom_headers=None):
    url = globalval.http_prefix + uri
    if method == "GET":
        try:
            resp = requests.get(url, headers=custom_headers, params=payload, timeout=3)
        except BaseException:
            resp = requests.get(url, headers=custom_headers, params=payload, timeout=3)
    if method == "POST":
        headers = {"Content-Type": "application/json"}
        if custom_headers:
            headers.update(custom_headers)
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=3)
        except BaseException:
            resp = requests.post(url, json=payload, headers=headers, timeout=3)
    return resp.json()

