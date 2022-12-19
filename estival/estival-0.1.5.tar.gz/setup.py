# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['estival', 'estival.calibration.mcmc']

package_data = \
{'': ['*']}

install_requires = \
['arviz>=0.12.1', 'numpy>=1.20.3', 'scipy>=1.7.3']

setup_kwargs = {
    'name': 'estival',
    'version': '0.1.5',
    'description': 'A set of calibration and probabilistic programming tools for use with summerepi2',
    'long_description': '# estival\nCalibration and optimization tools for summer\n\nA minimal pip-installable package providing MCMC and support tools for use with the summer2 library \n\nBased on the AuTuMN calibration module\n\nhttps://github.com/monash-emu/AuTuMN\n',
    'author': 'David Shipman',
    'author_email': 'dshipman@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/monash-emu/estival',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.0,<3.11',
}


setup(**setup_kwargs)
