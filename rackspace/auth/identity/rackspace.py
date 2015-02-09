# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Rackspace authorization plugins.
TODO
"""

import logging

from openstack.auth import access
from openstack.auth.identity import base
from openstack import exceptions

_logger = logging.getLogger(__name__)


class Auth(base.BaseIdentityPlugin):

    #: Valid options for this plugin
    valid_options = [
        "auth_url",
        "user_name",
        "password",
        "api_key",
        "token",
        "tenant_id",
        "tenant_name",
        "reauthenticate"
    ]

    def __init__(self, auth_url, user_name=None, password="", api_key="",
                 token=None, tenant_id=None, tenant_name=None,
                 reauthenticate=True):

        super(Auth, self).__init__(auth_url=auth_url,
                                   reauthenticate=reauthenticate)

        if not (user_name or token):
            msg = "You must specify either a user_name or token"
            raise exceptions.AuthorizationFailure(msg)

        if ((tenant_id and tenant_name) or
           (token and not any([tenant_id, tenant_name]))):
            msg = "Only one of tenant_name and tenant_id can be specified."
            raise exceptions.AuthorizationFailure(msg)

        self.user_name = user_name
        self.password = password
        self.api_key = api_key
        self.token = token
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name

    def authorize(self, transport, **kwargs):
        """Obtain access information from Rackspace."""
        headers = {"Content-type": "application/json"}
        url = self.auth_url.rstrip('/') + '/tokens'
        params = {'auth': self.get_auth_data(headers)}

        _logger.debug('Making authentication request to %s', url)
        resp = transport.post(url, json=params, headers=headers)

        try:
            resp_data = resp.json()['access']
        except (KeyError, ValueError):
            raise exceptions.InvalidResponse(response=resp)

        return access.AccessInfoV2(**resp_data)

    def get_auth_data(self, headers):
        """Identity v2 token authentication data."""
        if self.token is None:
            if self.password:
                data = {"passwordCredentials":
                        {"username": self.user_name,
                         "password": self.password}}
            elif self.api_key:
                data = {"RAX-KSKEY:apiKeyCredentials":
                        {"username": self.user_name, "apiKey": self.api_key}}

            if self.tenant_name:
                data["tenantName"] = self.tenant_name
            elif self.tenant_id:
                data["tenantId"] = self.tenant_id

            return data
        else:
            data = {"token": {"id": self.token}}

            if self.tenant_id:
                data["tenantId"] = self.tenant_id
            elif self.tenant_name:
                data["tenantName"] = self.tenant_name

            return data

    def invalidate(self):
        """Invalidate the current authentication data."""
        if super(Auth, self).invalidate():
            self.token = None
            self.access_info = None
            return True
        return False
