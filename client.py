# -*- coding: utf-8 -*-

from client_base import AppfClientBase, ContrailClientBase

class AppfClient(AppfClientBase):
    ''' AppfClient
    Python wrapper for Appformix API v1/v2
    '''
    def get_report(self, params=None, headers=None):
        ''' Get department/report
        '''
        return self.get("/reports/department", params, headers)

    def get_token(self, params=None, headers=None):
        ''' Post /auth_credentials
        '''
        return self.post("/auth_credentials", params, headers, apiv='v1')

    def auth_token(self, params=None, headers=None):
        ''' Post /auth_credentials
        '''
        return self.post("/auth_token", params, headers, apiv='v2')

class ContrailClient(ContrailClientBase):
    ''' ContrailClient
    Python wrapper for Contrail config/analytics API v1/v2
    '''
    def get_token(self, params=None, headers=None):
        ''' Post /v3/auth/tokens
        '''
        return self.post("/v3/auth/tokens", params, headers, api='keystone')

    def auth_token(self, params=None, headers=None):
        ''' Post /v3/auth_credentials
        '''
        return self.get("/v3/auth/tokens", params, headers, api='keystone')

    def get_bgppeer(self, params=None, headers=None):
        ''' Get /analytics/uves/control-node/overcloud-contrailcontroller-0
        '''
        return self.get("/analytics/uves/control-node/overcloud-contrailcontroller-0", params, headers, api='analytics')

    def get_virtual_networks(self, params=None, headers=None):
        ''' Get /analytics/uves/virtual-networks
        '''
        return self.get("/analytics/uves/virtual-networks", params, headers, api='analytics')
