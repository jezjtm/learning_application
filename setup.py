from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in learning_application/__init__.py
from learning_application import __version__ as version

setup(
	name='learning_application',
	version=version,
	description='GC',
	author='bizkit',
	author_email='learning_application@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
