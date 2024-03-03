# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clandestino_postgres']

package_data = \
{'': ['*']}

install_requires = \
['clandestino-interfaces>=0.1.0,<0.2.0',
 'psycopg[binary]>=3.1.18,<4.0.0',
 'python-decouple>=3.8,<4.0']

setup_kwargs = {
    'name': 'clandestino-postgres',
    'version': '0.1.1',
    'description': 'Clandestino Postgres implementation',
    'long_description': '# Clandestino Post\n\nMain project [here](https://github.com/CenturyBoys/clandestino)\n\nThis project uses [motor](https://pypi.org/project/motor/) "^3.3.2" package to communicate with mongodb.\n\nmotor = "^3.3.2"',
    'author': 'XimitGaia',
    'author_email': 'im.ximit@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
