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
from rackspace.backup import backup_service


class RestoreConfiguration(resource.Resource):
    id_attribute = 'BackupId'
    base_path = 'restore'
    service = backup_service.BackupService()

    # capabilities
    allow_create = True
    allow_update = True

    # Properties
    #: ID that uniquely identifies a Cloud Backup agent
    agent_id = resource.prop('MachineAgentId')
    #: Cloud Backup agent's name
    agent_name = resource.prop('BackupMachineName')
    #: Indicates the backup configuration ID for a backup
    backup_configuration_id = resource.prop('BackupConfigurationId')
    #: Indicates the backup configuration name for a backup
    backup_configuration_name = resource.prop('BackupConfigurationName')
    #: Identifies a unique backup
    backup_id = resource.prop('BackupId')
    #: Indicates if files are overwritten. Valid values are:
    #: ``true`` or ``false``.
    can_overwrite = resource.prop('OverwriteFiles')
    #: Specifies the datacenter where the original machine agent that was
    #: responsible for creating the backup, that is being used for the restore,
    #: is or was located (the source machine does not have to be online).
    datacenter = resource.prop('BackupDataCenter')
    #: Identifies the machine to which you want the backups to restore
    destination_agent_id = resource.prop('DestinationMachineId')
    #: Name of the machine to which you want the backups to restore
    destination_agent_name = resource.prop('DestinationMachineName')
    #: Specifies the path where you want the backup to restore
    destination_path = resource.prop('DestinationPath')
    #: Encrypted password. Valid values are:
    #: ``null`` or ``string``.
    encrypted_password = resource.prop('EncryptedPassword')
    #: Indicates the list of files and folders not to back up. *Type: list*
    exclusions = resource.prop('Exclusions', type=list)
    #: Type of server. Valid values are:
    #: ``RaxCloudServer``: Rackspace Cloud Servers
    flavor = resource.prop('BackupFlavor')
    #: Indicates the list of files and folders to back up. *Type: list*
    inclusions = resource.prop('Inclusions', type=list)
    #: Indicates if backups are encrypted. Valid values are:
    #: ``true`` or ``false``.
    is_encrypted = resource.prop('IsEncrypted')
    #: Public key of the public/private encryption key pair
    public_key = resource.prop('PublicKey')
    #: Identifies a restore configuration
    restore_id = resource.prop('RestoreId')
    #: Identifies the machine where your backup was originally made
    source_agent_id = resource.prop('BackupMachineId')
    #: Indicates the current state. Valid values are:
    #: ``0``: Creating
    #: ``1``: Queued
    #: ``2``: InProgress
    #: ``3``: Completed
    #: ``4 `: stopped
    #: ``5 `: Failed
    #: ``6 `: StartRequested
    #: ``7 `: StopRequested
    #: ``8 `: Completed WithErrors
    #: ``9 `: Preparing
    status = resource.prop('RestoreStateId')
    #: Indicates the timestamp of the backup
    timestamp = resource.prop('BackupRestorePoint')
