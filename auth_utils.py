# -*- coding: utf-8 -*-

import json
import config_util
from client import AppfClient, ContrailClient
from datetime import datetime as dt
from pytz import timezone

class Appf_auth_utils():

    def __init__(self):
        # Get some value from config.
        self.host = config_util.get('DEFAULT', 'auth_host')
        self.user = config_util.get('DEFAULT', 'user')
        self.password = config_util.get('DEFAULT', 'password')
        self.path = config_util.get('DEFAULT', 'cache_file')
        self.client = AppfClient()
        self.params =\
        {
            "UserDomainName": "Default",
            "UserName": self.user,
            "ProjectName":'admin',
            "AuthType": "openstack",
            "Password": self.password,
            "ProjectDomainName": "Default"
        }

    def get_token_and_cache(self):
        # Write token to cache if succeed in acquiring token.
        print('Get new token')
        res = self.client.get_token(self.params)
        if res.status_code == 200:
            token = json.loads(res.content)["Token"]["tokenId"]
            with open(self.path, mode='w') as f:
                f.write(token)
            return token
        else:
            print("Responce: " + str(res.status_code))
            print("Authentication Failed")
            exit(1)

    def check_cache(self):
        # Check cache file and validate token.
        try:
            f = open(self.path)
        except IOError:
            print('Token cache was not found')
            token = self.get_token_and_cache()
            return token
        else:
            with f:
                token = f.read()
            params = {
                "AuthType": "openstack",
                "Token": token
            }
            res = self.client.auth_token(params=params)
            if res.status_code == 200:
                res = json.loads(res.content)
                expire_time = res["Token"]["expiresAt"]
                expire_time = dt.strptime(expire_time, '%Y-%m-%dT%H:%M:%S.000000Z')
                local_time = dt.now(timezone('UTC')).strftime("%Y-%m-%d %H:%M:%S")
                local_time = dt.strptime(local_time, '%Y-%m-%d %H:%M:%S')

                if local_time >= expire_time:
                    token = self.get_token_and_cache()
                    return token
                else:
                    return token
            else:
                print('Get new token')
                token = self.get_token_and_cache()
                return token

class Contrail_auth_utils():

    def __init__(self):
        # Get some value from config.
        self.host = config_util.get('DEFAULT', 'auth_host')
        self.user = config_util.get('DEFAULT', 'user')
        self.password = config_util.get('DEFAULT', 'password')
        self.path = config_util.get('DEFAULT', 'cache_file')

        self.client = ContrailClient()
        self.params = \
            {
                "auth": {
                    "scope": {
                        "project": {
                            "name": "admin",
                            "domain": {
                                "name": "Default"
                            }
                        }
                    },
                    "identity": {
                        "methods": [
                            "password"
                        ],
                        "password": {
                            "user": {
                                "name": self.user,
                                "password": self.password,
                                "domain": {
                                    "name": "default"
                                }
                            }
                        }
                    }
                }
            }

    def get_token_and_cache(self):
        # Write token to cache if succeed in acquiring token.
        print('Get new token')
        res = self.client.get_token(self.params)

        if res.status_code == 201:
            token = (res.headers['X-Subject-Token'])
            with open(self.path, mode='w') as f:
                f.write(token)
            return token
        else:
            print("Responce: " + str(res.status_code))
            print("Authentication Failed")
            exit(1)

    def check_cache(self):
        # Check cache file and validate token.
        try:
            f = open(self.path)
        except IOError:
            print('Token cache was not found')
            token = self.get_token_and_cache()
            return token
        else:
            with f:
                token = f.read()
            headers = {
                "X-Auth-Token": token,
                "X-Subject-Token": token
            }
            res = self.client.auth_token(headers=headers)
            if res.status_code == 200:
                print('Found token')
                return token
            else:
                token = self.get_token_and_cache()
                return token

