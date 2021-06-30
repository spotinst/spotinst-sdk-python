# Always prefer setuptools over distutils
from codecs import open
from os import path

import sys

from setuptools import setup

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

here = path.abspath(path.dirname(__file__))

# Get the long description from the README.md file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = {}
with open("spotinst_sdk2/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='spotinst-sdk2',

    version=version['__version__'],

    description='A Python SDK for Spotinst',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url='https://github.com/spotinst/spotinst-sdk-python',

    # Author details
    author='Spotinst',
    author_email='service@spotinst.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ],

    keywords='spotinst spot instances aws ec2 cloud infrastructure development elastigroup',
    packages=[
    "spotinst_sdk2", 
        "spotinst_sdk2.clients", 
            "spotinst_sdk2.clients.admin",
            "spotinst_sdk2.clients.elastigroup",
            "spotinst_sdk2.clients.functions",
            "spotinst_sdk2.clients.mcs",
            "spotinst_sdk2.clients.mlb",
            "spotinst_sdk2.clients.mrscaler",
            "spotinst_sdk2.clients.ocean",
            "spotinst_sdk2.clients.subscription",
            "spotinst_sdk2.clients.setup",
            "spotinst_sdk2.clients.managed_instance",
        "spotinst_sdk2.models",
            "spotinst_sdk2.models.admin",
            "spotinst_sdk2.models.elastigroup",
                "spotinst_sdk2.models.elastigroup.aws",
                "spotinst_sdk2.models.elastigroup.azure",
                "spotinst_sdk2.models.elastigroup.gcp",
            "spotinst_sdk2.models.functions",
            "spotinst_sdk2.models.mlb",
            "spotinst_sdk2.models.mrscaler",
                "spotinst_sdk2.models.mrscaler.aws",
            "spotinst_sdk2.models.ocean",
                "spotinst_sdk2.models.ocean.aws",
            "spotinst_sdk2.models.setup",
                "spotinst_sdk2.models.setup.azure",
                "spotinst_sdk2.models.setup.gcp",
            "spotinst_sdk2.models.subscription",
            "spotinst_sdk2.models.managed_instance",
                "spotinst_sdk2.models.managed_instance.aws",
    ],
    install_requires=['requests', 'PyYaml'],

    setup_requires=[] + pytest_runner,
    tests_require=["pytest"]
)
