# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in pathology_management/__init__.py
from pathology_management import __version__ as version

setup(
	name='pathology_management',
	version=version,
	description='Pathology Management',
	author='Frappe',
	author_email='manjari.mahulikar@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
