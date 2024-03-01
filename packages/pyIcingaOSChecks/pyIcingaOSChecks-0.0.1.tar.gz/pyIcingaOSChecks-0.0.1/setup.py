from setuptools import setup, find_packages


setup(
    name='pyIcingaOSChecks',
    description='Icinga2 Check OS Checks for pyIcingaFramework',
    long_description='Icinga2 checks for local OS',
    author='Paul Denning',
    version='0.0.1',
    include_package_data=True,
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        "pyIcingaFramework",
        "psutil",
        "dbus-python",
    ],
    keywords=['icinga2', 'nagios'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
)