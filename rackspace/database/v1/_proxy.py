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

from openstack.database.v1 import _proxy
from openstack.database.v1 import database
from openstack.database.v1 import flavor
from openstack.database.v1 import instance
from openstack.database.v1 import user

from rackspace.database import database_service
from rackspace.database.v1 import backup
from rackspace.database.v1 import backup_schedule


database.Database.service = database_service.DatabaseService()
flavor.Flavor.service = database_service.DatabaseService()
instance.Instance.service = database_service.DatabaseService()
user.User.service = database_service.DatabaseService()


class Proxy(_proxy.Proxy):

    def __init__(self, session):
        super(Proxy, self).__init__(session)

    def backups(self, **query):
        """Return a generator of database backups

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of database backups
        :rtype: :class:`~rackspace.database.v1.backup.Backup`
        """
        return self._list(backup.Backup, paginated=False, **query)

    def create_backup(self, **attrs):
        """Create a new backup from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~rackspace.database.v1.backup.Backup`,
                           comprised of the properties on the Backup class.

        :returns: The results of database backup creation
        :rtype: :class:`~rackspace.database.v1.backup.Backup`
        """
        return self._create(backup.Backup, **attrs)

    def delete_backup(self, value, ignore_missing=True):
        """Delete a database backup

        :param value: The value can be either the ID of a backup or a
               :class:`~rackspace.database.v1.backup.Backup` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the backup does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent backup.

        :returns: ``None``
        """
        self._delete(backup.Backup, value, ignore_missing=ignore_missing)

    def find_backup(self, name_or_id, ignore_missing=True):
        """Find a single database backup

        :param name_or_id: The name or ID of a backup.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.database.v1.backup.Backup` or None
        """
        return backup.Backup.find(self.session, name_or_id,
                                  ignore_missing=ignore_missing)

    def get_backup(self, value):
        """Get a single database backup

        :param value: The value can be the ID of a backup or a
                      :class:`~rackspace.database.v1.backup.Backup`
                      instance.
        :returns: One :class:`~rackspace.database.v1.backup.Backup`

        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(backup.Backup, value)

    def backup_schedules(self, **query):
        """Return a generator of database backup schedules

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.
        :returns: A generator of database backup schedules objects

        :rtype: :class:`~rackspace.database.v1.backup_schedule.BackupSchedule`
        """
        return self._list(backup_schedule.BackupSchedule,
                          paginated=False, **query)

    def create_backup_schedule(self, **attrs):
        """Create a new database backup schedule from attributes

        :param dict attrs: Keyword arguments which will be used to create a
            :class:`~rackspace.database.v1.backup_schedule.BackupSchedule`,
            comprised of the properties on the BackupSchedule class.
        :returns: The results of database backup schedule creation

        :rtype: :class:`~rackspace.database.v1.backup_schedule.BackupSchedule`
        """
        return self._create(backup_schedule.BackupSchedule, **attrs)

    def delete_backup_schedule(self, value, ignore_missing=True):
        """Delete a database backup schedule

        :param value: The value can be either the ID of a backup schedule or
            a :class:`~rackspace.database.v1.backup_schedule.BackupSchedule`
            instance.
        :param bool ignore_missing: When set to ``False``
                :class:`~openstack.exceptions.ResourceNotFound` will be raised
                when the database backup schedule does not exist. When set to
                ``True``, no exception will be set when attempting to delete a
                nonexistent database backup schedule.

        :returns: ``None``
        """
        self._delete(backup_schedule.BackupSchedule, value,
                     ignore_missing=ignore_missing)

    def find_backup_schedule(self, name_or_id, ignore_missing=True):
        """Find a single database backup schedule

        :param name_or_id: The name or ID of a database backup schedule.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist. When set to
                    ``True``, None will be returned when attempting to find
                    a nonexistent resource.

        :returns: One :class:`~rackspace.database.v1
                               .backup_schedule.BackupSchedule` or None
        """
        return backup_schedule.BackupSchedule.find(
            self.session, name_or_id, ignore_missing=ignore_missing)

    def get_backup_schedule(self, value):
        """Get a single database backup schedule

        :param value: The value can be the ID of a database backup schedule or
                      a :class:`~rackspace.database
                                 .v1.backup_schedule.BackupSchedule` instance.

        :returns: One :class:`~rackspace.database
                               .v1.backup_schedule.BackupSchedule`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(backup_schedule.BackupSchedule, value)

    def update_backup_schedule(self, value, **attrs):
        """Update a database backup schedule

        :param value: Either the id of a database backup schedule instance or
                      a :class:`~rackspace.database
                                 .v1.backup_schedule.BackupSchedule` instance.
        :attrs kwargs: The attributes to update on the instance represented
                       by ``value``.

        :returns: The updated database backup schedule
        :rtype: :class:`~rackspace.database.v1.backup_schedule.BackupSchedule`
        """
        return self._update(backup_schedule.BackupSchedule, value, **attrs)
