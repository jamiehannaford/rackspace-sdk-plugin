Rackspace Plugin for the OpenStack SDK
======================================

.. image:: https://travis-ci.org/rackerlabs/rackspace-sdk-plugin.svg?branch=master
    :target: https://travis-ci.org/rackerlabs/rackspace-sdk-plugin

This plugin enables support for Rackspace authentication and services
with the
`OpenStack SDK <https://pypi.python.org/pypi/python-openstacksdk>`_.

Usage
-----

The following example connects to the Rackspace cloud and lists containers
stored in Cloud Files within the IAD datacenter. ::

   from openstack import connection
   from openstack import profile

   prof = profile.Profile(extensions=["rackspace"])
   prof.set_region(prof.ALL, "IAD")

   conn = connection.Connection(profile=prof,
                                auth_plugin="rackspace",
                                username="my_user",
                                api_key="123abc456def789ghi")

   for container in conn.object_store.containers():
       print(container.name)

Documentation
-------------

Rackspace-specific documentation is not currently available.

Documentation for the OpenStack SDK is available at
http://python-openstacksdk.readthedocs.org/en/latest/

Requirements
------------

* Python 2.7+, Python 3.3+
* python-openstacksdk>=0.5

License
-------

Apache 2.0

Release Notes
=============

0.2.0
-----

* Changed UserPreference to Profile as was done in version 0.5 of the SDK.

0.1.0
-----

* Changed plugin style to match OpenStack SDK's shift to python-keystoneclient
  styled authentication plugins.

.. note:: This release is incompatible with 0.0.1. The ``user_name``
          authentication parameter has changed to ``username``.

0.0.1
-----

* Initial release
* Support for password, API key, and token authentication
* Support for Cloud Files Bulk Delete
