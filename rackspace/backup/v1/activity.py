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


class Activity(resource.Resource):
    id_attribute = 'ID'
    base_path = 'activity'
    service = backup_service.BackupService()

    # capabilities
    allow_list = True

    # Properties
    #: Indicates the backup configuration ID for a backup
    backup_configuration = resource.prop('ParentId')
    #: Specifies the backup ID associated with a restore
    backup_id = resource.prop('BackupId')
    #: Indicates the machine agent ID of the source system
    destination_agent_id = resource.prop('DestinationMachineAgentId')
    #: Indicates the machine agent ID of the source system
    destination_agent_name = resource.prop('DestinationMachineName')
    #: Indicates the backup name or restore name
    name = resource.prop('DisplayName')
    #: Indicates the machine agent ID of the source system
    source_agent_id = resource.prop('SourceMachineAgentId')
    #: Indicates the machine agent ID of the source system
    source_agent_name = resource.prop('SourceMachineName')
    #: Indicates the current state. Valid values are:
    #: Creating, Queued, InProgress, Completed, Stopped, Failed,
    #: startRequested, Stoprequested, Completed WithErrors, and Preparing.
    status = resource.prop('CurrentState')
    #: Indicates the time of the activity
    time = resource.prop('TimeOfActivity')
    #: Specifies type of activity.
    #: Valid values are Restore, Backup, or Cleanup.
    type = resource.prop('Type')
