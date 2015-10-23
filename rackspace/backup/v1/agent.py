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

from openstack import resource
from openstack import utils
from rackspace.backup import backup_service


class Agent(resource.Resource):
    id_attribute = 'MachineAgentId'
    base_path = '/user/agents'
    service = backup_service.BackupService()

    # capabilities
    allow_delete = True
    allow_list = True

    # Properties
    #: Indicates whether a cleanup can be manually triggered
    #: on the backup vault
    cleanup = resource.prop('CleanupAllowed')
    #: Full public URI for Cloud Files where backups are stored for this agent
    container = resource.prop('BackupContainer')
    #: Data center where the Cloud Server is located.
    #: Valid values are IAD, ORD, DFW, HKG, LON, or SYD).
    datacenter = resource.prop('BackupDatacenter')
    #: Indicates if the Rackspace Cloud Backup agent on the server is disabled
    disabled = resource.prop('IsDisabled')
    #: Indicates if backups are encrypted. Valid values are true or false.
    encrypted = resource.prop('IsEncrypted')
    #: Flavor: 'RaxCloudServer' for Rackspace Cloud Servers
    flavor = resource.prop('Flavor')
    #: Public key of the public/private encryption key pair
    public_key = resource.prop('PublicKey')
    #: Base architecture of the Cloud Server.
    #: Valid values are 64-bit or 32-bit.
    server_arch = resource.prop('Architecture')
    #: Name of the Cloud Server
    server_name = resource.prop('MachineName')
    #: Operating system of Cloud Server
    server_os = resource.prop('OperatingSystem')
    #: Operating system version of Cloud Server
    server_os_version = resource.prop('OperatingSystemVersion')
    #: Public IPv4 address of the Cloud Server
    server_ipaddress = resource.prop('IPAddress')
    #: ID that uniquely identifies a Cloud Backup agent
    server_uuid = resource.prop('HostServerId')
    #: Indicates if the Cloud Backup agent is using ServiceNet
    #: to backup data to Cloud Files
    servicenet = resource.prop('UseServiceNet')
    #: Status of the Cloud Backup agent. Valid values are Online or Offline.
    status = resource.prop('Status')
    #: Time of last successful backup
    time = resource.prop('TimeOfLastSuccessfulBackup')
    #: Size of backup data in MB
    vault_size = resource.prop('BackupVaultSize')
    #: Version of the Rackspace Cloud Backup agent
    version = resource.prop('AgentVersion')

    def disable(self, session):
        """Disable agent.

        This operation disables the Cloud Backup agent.
        Disabling an agent does not delete it or its data.
        You can re-enable disabled agents later.
        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``None``
        """
        body = {'MachineAgentId': self.id, "Enable": True}
        url = utils.urljoin('agent', 'enable')
        session.post(url, service=self.service, accept=None, json=body)

    def enable(self, session):
        """Enable agent.

        This operation enables the Cloud Backup agent.
        Disabling an agent does not delete it or its data.
        You can re-enable disabled agents later.
        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``None``
        """
        body = {'MachineAgentId': self.id, "Enable": False}
        url = utils.urljoin('agent', 'enable')
        session.post(url, service=self.service, accept=None, json=body)
