from distutils.core import setup
from setuptools import find_packages

setup_args = {
    'name': 'ethereum-bip44-python',
    'version': '0.1',
    'packages': find_packages(),
}

install_requires = [
    'rlp',
    'eth_utils',
    'two1',
    'pycrypto',
    'pycryptodome',
]

setup_args['install_requires'] = install_requires

setup(**setup_args)
