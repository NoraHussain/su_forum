from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in su_forum/__init__.py
from su_forum import __version__ as version

setup(
	name="su_forum",
	version=version,
	description="Forum",
	author="su",
	author_email="su@su.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
