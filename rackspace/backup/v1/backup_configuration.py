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


class BackupConfiguration(resource.Resource):
    id_attribute = 'BackupConfigurationId'
    base_path = 'backup-configuration'
    service = backup_service.BackupService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_retrieve = True
    allow_update = True

    # Properties
    #: Indicates if a backup configuration is active.
    active = resource.prop('IsActive')
    #: ID that uniquely identifies a Cloud Backup agent
    agent_id = resource.prop('MachineAgentId')
    #: Indicates if the backup configuration is deleted
    deleted = resource.prop('IsDeleted')
    #: Indicates if backups are encrypted. Valid values are true or false.
    encrypted = resource.prop('IsEncrypted')
    #: Flavor: 'RaxCloudServer' for Rackspace Cloud Servers
    flavor = resource.prop('Flavor')
    #: Frequency of backup schedule.
    #: Valid values are "Manually", "Hourly", "Daily", and "Weekly"
    frequency = resource.prop('Frequency')
    #: Specifies when to send notification. Valid values are as follows:
    #: 1 = notifications are sent as soon as possible
    #: 2 = notifications are sent at the next scheduled time
    missed_backup_action = resource.prop('MissedBackupActionId')
    #: The name of the backup configuration. The configuration typically has
    #: the backup schedule, files to backup, and notification options.
    name = resource.prop('BackupConfigurationName')
    #: Indicates how many days backup revisions are maintained.
    #: Valid values are 0, 30 , and 60. 0 means indefinite.
    retention = resource.prop('VersionRetention')
    #: Uniquely identifies the schedule that is associated
    #: with this configuration
    schedule = resource.prop('BackupConfigurationScheduled')
