# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clandestino_elasticsearch']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.9.3,<4.0.0',
 'clandestino-interfaces>=0.1.0,<0.2.0',
 'elasticsearch>=8.12.1,<9.0.0',
 'python-decouple>=3.8,<4.0']

setup_kwargs = {
    'name': 'clandestino-elasticsearch',
    'version': '0.1.0',
    'description': 'Clandestino Elasticsearch implementation',
    'long_description': '# Clandestino Elasticsearch\n\nMain project [here](https://github.com/CenturyBoys/clandestino)\n\nThis project uses [elasticsearch](https://pypi.org/project/elasticsearch/) "^8.12.1" and [aiohttp](https://pypi.org/project/aiohttp/) "^3.9.3" packages to communicate with elasticsearch.\n\n',
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
