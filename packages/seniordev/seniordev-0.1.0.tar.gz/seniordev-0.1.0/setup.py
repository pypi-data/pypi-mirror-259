# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seniordev']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'seniordev',
    'version': '0.1.0',
    'description': 'Add senior python dev for all projects - trust is here',
    'long_description': None,
    'author': 'Dmitriy Komarovskiy',
    'author_email': 'dmitriy.komarovskiy@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
