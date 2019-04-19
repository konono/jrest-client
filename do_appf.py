# -*- coding: utf-8 -*-

from client import AppfClient
from auth_utils import Appf_auth_utils
import json

params = {
    "month": "3",
    "year": "2019",
}

auth_utils = Appf_auth_utils()
token = auth_utils.check_cache()
print(token)
client = AppfClient(token)
res = client.get_report(params)
response_json = json.loads(res.content)
print(response_json)
