# -*- coding: utf-8 -*-
"""Top-level package for {{ cookiecutter.project_name }}."""
VERSION = tuple('{{cookiecutter.version}}'.split('.'))


__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
# string created from tuple to avoid inconsistency
__version__ = ".".join([str(x) for x in VERSION])

