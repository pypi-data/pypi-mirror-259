from datetime import datetime
from mixin_sdk.request import request


def get_network_snapshots(offset, asset = None, limit = 10, order = "DESC"):
    '''
    return snapshots of mixin network
    :param offset: string, format RFC3339Nano, UTC or non UTC time
    :param asset : string, asset id of mixin network, eg: c6d0c728-2624-429b-8e0d-d9d19b6592fa for BTC, default None
    :param limit: interger, max 500
    :param order: DESC or ASC, DESC for snapshots before offset time ; ASC for snapshots after offset time
    '''
    if limit > 500:
        limit = 500
    if order not in ["DESC", "ASC"]:
        order = "DESC"
    payload = {"limit": limit, "offset": offset, "order": order}
    uri = "/network/snapshots"
    data = request(uri=uri, method="GET", payload=payload)
    if data:
        return data['data']
    else:
        return None


def get_user_snapshots(offset, access_token, asset=None, limit=10, opponent=None):
    if limit > 500:
        limit = 500
    payload = {"limit": limit, "offset": offset, 'asset': asset, 'opponent': opponent}
    uri = "/snapshots"
    data = request(uri=uri, method="GET", payload=payload, custom_headers={"Authorization": "Bearer " + access_token})
    return data['data']

