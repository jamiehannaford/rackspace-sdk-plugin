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
    #: Identifies a unique backup
    backup = resource.prop('BackupId')
    #: Specifies the datacenter where the original machine agent
    #: that was responsible for creating the backup, that is being used
    #: for the restore, is or was located
    #: (the source machine does not have to be online).
    datacenter = resource.prop('BackupDataCenter')
    #: Identifies the machine to which you want the backups to restore
    destination_agent_id = resource.prop('DestinationMachineId')
    #: Specifies the path where you want the backup to restore
    destination_path = resource.prop('DestinationPath')
    #: Indicates if files are overwritten
    overwrite = resource.prop('OverwriteFiles')
    #: Identifies the machine where your backup was originally made
    source_agent_id = resource.prop('BackupMachineId')
