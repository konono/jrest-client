# -*- coding: utf-8 -*-

import requests
import config_util

class AppfClientBase:

    '''
    Python Client Base for Appformix API v1/2
    '''

    USER_AGENT = 'Appfclient python3 binding'
    ACCEPT = 'application/json, text/plain, */*'
    HEADER = {
        'Accept': ACCEPT,
        'User-Agent': USER_AGENT,
        "Content-Type": "application/json;charset=utf-8",
    }

    def __init__(self, token=None):
        self.token = token
        self.host = config_util.get('DEFAULT', 'appf_host')

    def _url_prefix(self, apiv):
        ''' url prefix for api endpoint
        '''
        if apiv is None:
            return '{}/appformix/controller/v2.0/'.format(self.host)
        else:
            return '{}/appformix/v1.0/'.format(self.host)


    def header(self):
        ''' make request header
        '''

        if self.token:
            self.HEADER.update(
                {"X-Auth-Type": "openstack",
                 "X-Auth-Token": self.token,})
        return self.HEADER

    def _request(self, method, url, params=None, headers=None):
        ''' alias for request with requests module
        Returns requests.models.Response instance
        :param method: "GET", "POST", "PUT", "DELETE", "PATCH"
        :param url: request url
        :param params: dictionary to be sent
        :param headers: dictionary of Http Headers to be sent
        '''
        headers = self.header() if headers is None else headers
        if type(headers) is not dict:
            return TypeError('headers must be dictionary')

        method = method.upper()
        if method in ('GET', 'DELETE'):
            response = requests.request(
                method=method, url=url, headers=headers, params=params)

        elif method in ('POST', 'PUT', 'PATCH'):
            response = requests.request(
                method=method, url=url, headers=headers, json=params)

        else:
            raise Exception('Unknown method')

        if response.ok:
            return response

        else:
            print('Request Failed {}'.format(response.status_code))
            return response

    def request(self, method, path, params=None, headers=None, apiv=None):
        ''' alias for request with self._request method
        Returns requests.models.Response instance
        :param method: "GET", "POST", "PUT", "DELETE", "PATCH"
        :param path: request path for AppF api (e.g. /reports/department)
        :param params: dictionary to be sent
        :param headers: dictionary of Http Headers to be sent
        '''
        url = self._url_prefix(apiv) + path
        return self._request(method, url, params, headers)

    def get(self, path, params=None, headers=None, apiv=None):
        ''' get request
        '''
        return self.request('GET', path, params, headers, apiv)

    def post(self, path, params=None, headers=None, apiv=None):
        ''' post request
        '''
        return self.request('POST', path, params, headers, apiv)

    def put(self, path, params=None, headers=None, apiv=None):
        ''' put request
        '''
        return self.request('PUT', path, params, headers, apiv)

    def patch(self, path, params=None, headers=None, apiv=None):
        ''' patch request
        '''
        return self.request('PATCH', path, params, headers, apiv)

    def delete(self, path, params=None, headers=None, apiv=None):
        ''' delete request
        '''
        return self.request('DELETE', path, params, headers, apiv)

class ContrailClientBase:

    '''
    Python Client Base for Contrail Config/Analytics API
    '''

    USER_AGENT = 'Contrailclient python3 binding'
    ACCEPT = 'application/json, text/plain, */*'
    HEADER = {
        'Accept': ACCEPT,
        'User-Agent': USER_AGENT,
        "Content-Type": "application/json;charset=utf-8",
    }

    def __init__(self, token=None):
        self.token = token

    def _url_prefix(self, api):
        ''' url prefix for api endpoint
        '''

        if api == 'keystone':
            self.host = config_util.get('DEFAULT', 'auth_host')
        elif api == 'config':
            self.host = config_util.get('DEFAULT', 'config_host')
        elif api == 'analytics':
            self.host = config_util.get('DEFAULT', 'analytics_host')
        else:
            print('Unsupported api type')

        return '{}'.format(self.host)

    def header(self):
        ''' make request header
        '''

        if self.token:
            self.HEADER.update(
                {"X-Auth-Token": self.token,})
        return self.HEADER

    def _request(self, method, url, params=None, headers=None):
        ''' alias for request with requests module
        Returns requests.models.Response instance
        :param method: "GET", "POST", "PUT", "DELETE", "PATCH"
        :param url: request url
        :param params: dictionary to be sent
        :param headers: dictionary of Http Headers to be sent
        '''
        headers = self.header() if headers is None else headers
        if type(headers) is not dict:
            return TypeError('headers must be dictionary')

        method = method.upper()
        if method in ('GET', 'DELETE'):
            response = requests.request(
                method=method, url=url, headers=headers, params=params)

        elif method in ('POST', 'PUT', 'PATCH'):
            response = requests.request(
                method=method, url=url, headers=headers, json=params)

        else:
            raise Exception('Unknown method')

        if response.ok:
            return response

        else:
            print('Request Failed {}'.format(response.status_code))
            return response

    def request(self, method, path, params=None, headers=None, api=None):
        ''' alias for request with self._request method
        Returns requests.models.Response instance
        :param method: "GET", "POST", "PUT", "DELETE", "PATCH"
        :param path: request path for AppF api (e.g. /reports/department)
        :param params: dictionary to be sent
        :param headers: dictionary of Http Headers to be sent
        '''
        url = self._url_prefix(api) + path
        print(url)
        return self._request(method, url, params, headers)

    def get(self, path, params=None, headers=None, api=None):
        ''' get request
        '''
        return self.request('GET', path, params, headers, api)

    def post(self, path, params=None, headers=None, api=None):
        ''' post request
        '''
        return self.request('POST', path, params, headers, api)

    def put(self, path, params=None, headers=None, api=None):
        ''' put request
        '''
        return self.request('PUT', path, params, headers, api)

    def patch(self, path, params=None, headers=None, api=None):
        ''' patch request
        '''
        return self.request('PATCH', path, params, headers, api)

    def delete(self, path, params=None, headers=None, api=None):
        ''' delete request
        '''
        return self.request('DELETE', path, params, headers, api)
