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

from openstack import profile

from rackspace.object_store import object_store_service
from rackspace.message import message_service


class Profile(profile.Profile):

    def __init__(self):
        super(Profile, self).__init__()

        # Override with our implementation for Cloud Files
        cloud_files = object_store_service.ObjectStoreService()
        cloud_files.set_visibility(None)
        self._services[cloud_files.service_type] = cloud_files

        # Override with our implementation for Cloud Queues
        cloud_queues = message_service.MessageService()
        cloud_queues.set_visibility(None)
        self._services["messaging"] = cloud_queues
