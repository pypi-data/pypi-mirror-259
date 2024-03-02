# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clandestino_interfaces']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'clandestino-interfaces',
    'version': '0.1.1',
    'description': 'Clandestino base interfaces',
    'long_description': '# Clandestino Interfaces\n\nMain project [here](https://github.com/CenturyBoys/clandestino)\n\nBase package to allow main project and extras to import all interfaces an abstract classes without cicle import references.\n\nContent:\n\n- IMigrateRepository\n- MigrationStatus\n- AbstractMigration',
    'author': 'XimitGaia',
    'author_email': 'im.ximit@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
