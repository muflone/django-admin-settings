# Django Admin Settings
[![Travis CI Build Status](https://img.shields.io/travis/com/muflone/django-admin-settings/master.svg)](https://www.travis-ci.com/github/muflone/django-admin-settings)
[![CircleCI Build Status](https://img.shields.io/circleci/project/github/muflone/django-admin-settings/master.svg)](https://circleci.com/gh/muflone/django-admin-settings)

**Description:** A Django application to configure some Django Admin settings 

**Copyright:** 2023 Fabio Castelli (Muflone) <muflone@muflone.com>

**License:** GPL-3+

**Source code:** https://github.com/muflone/django-admin-settings

**Documentation:** http://www.muflone.com/django-admin-settings/

# Description

Django Admin Settings allows you to configure some settings in Django Admin.

# System Requirements

The Python dependencies for the server part are listed in the
`requirements.txt` file.

* Python >= 3.9
* Django 4.1.x (https://pypi.org/project/Django/)

# Installation

To install Django Admin Settings application you can configure the
`INSTALLED_APPS` setting like this:

```python
INSTALLED_APPS = [
    'django_admin_settings',
    ...
]
```

# Models

## ListDisplay

The `ListDisplay` models allows you to set the visible fields in the records
list page in Django Admin.

You can simply configure your models by settings:

- Model
- Field name
- Sort order number
- Active status
