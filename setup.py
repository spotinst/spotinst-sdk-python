# Always prefer setuptools over distutils
from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README.rst file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

version = {}
with open("spotinst_sdk/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='spotinst-sdk',

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
    packages=["spotinst_sdk"],
    install_requires=['requests', 'PyYaml'],

    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
