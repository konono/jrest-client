# -*- coding: utf-8 -*-

from auth_utils import Contrail_auth_utils
from client import ContrailClient


params={"cfilt": "BgpRouterState:num_bgp_peer"}

auth_utils = Contrail_auth_utils()
token = auth_utils.check_cache()
client = ContrailClient(token)
res = client.get_virtual_networks()
print(res.content)
res = client.get_bgppeer(params)
print(res.content)
