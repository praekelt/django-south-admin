Django South Admin
==================
**Django app allowing for South management through Admin.**

``django-south-admin`` allows you trigger `South <http://south.aeracode.org/>`_ migrations and manage migration histories through Django's admin interface.

``django-south-admin`` utilizes `django-object-tools <http://pypi.python.org/pypi/django-object-tools>`_ to hook into Django's admin interface and take care of user permissions.

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install ``django-object-tools`` as described `here <http://pypi.python.org/pypi/django-object-tools#id3>`_.

#. Install or add ``django-south-admin`` to your Python path.

#. Add ``south_admin`` to your ``INSTALLED_APPS`` setting.

Usage
-----

Once installed you should see a new *South* section on admin home. On the *Migration histories* listing view a new *Migrate* tool will be available allowing you to run South's ``migrate`` management command.

.. image:: https://github.com/downloads/praekelt/django-south-admin/migrate_example.png

If you don't see the tool make sure the logged in user has the appropriate *Can migrate migration historys* user permission assigned (or set user as superuser).

Clicking the *Migrate* tool link will immediatly kick-off South's ``migrate`` management command and return its output.

