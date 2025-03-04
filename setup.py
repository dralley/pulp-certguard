#!/usr/bin/env python3

from setuptools import setup, find_packages

requirements = [
    'PyOpenSSL',
    'pulpcore~=3.0rc7',
]

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='pulp-certguard',
    version='0.1.0rc3.dev',
    description='X.509 Certguards plugin for the Pulp Project',
    long_description=long_description,
    license='GPLv2+',
    author='Pulp Project Developers',
    author_email='pulp-list@redhat.com',
    url='http://www.pulpproject.org',
    python_requires='>=3.6',
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(exclude=['pulp_certguard.tests']),
    classifiers=(
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: POSIX :: Linux',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ),
    entry_points={
        'pulpcore.plugin': [
            'pulp_certguard = pulp_certguard:default_app_config',
        ]
    }
)
