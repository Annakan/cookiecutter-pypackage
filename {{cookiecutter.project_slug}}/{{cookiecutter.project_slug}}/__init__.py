# -*- coding: utf-8 -*-

# version as tuple for simple comparisons
VERSION = {% tuple({{cookiecutter.version}}.split('.')) %}

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
# string created from tuple to avoid inconsistency
__version__ = ".".join([str(x) for x in VERSION])

