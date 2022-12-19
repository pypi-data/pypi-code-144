# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blitzly', 'blitzly.etc', 'blitzly.plots']

package_data = \
{'': ['*']}

install_requires = \
['nbformat==5.7.0',
 'numpy==1.23.5',
 'pandas==1.5.2',
 'plotly==5.11.0',
 'scikit-learn==1.2.0']

setup_kwargs = {
    'name': 'blitzly',
    'version': '0.1.0',
    'description': 'Lightning-fast way to get plots with Plotly',
    'long_description': '<img src="https://github.com/invia-flights/blitzly/raw/main/docs/assets/images/icon.png" alt="blitzly logo" width="200" height="200"/><br>\n# blitzly ⚡️\n***Lightning-fast way to get plots with Plotly***\n\n[![Testing](https://github.com/invia-flights/blitzly/actions/workflows/testing.yml/badge.svg?branch=main)](https://github.com/invia-flights/blitzly/actions/workflows/testing.yml)\n[![pypi](https://img.shields.io/pypi/v/blitzly)](https://pypi.org/project/blitzly/)\n[![python version](https://img.shields.io/pypi/pyversions/blitzly?logo=python&logoColor=yellow)](https://www.python.org/)\n[![docs](https://img.shields.io/badge/docs-mkdoks%20material-blue)](https://invia-flights.github.io/blitzly/)\n[![license](https://img.shields.io/github/license/invia-flights/blitzly)](https://github.com/invia-flights/blitzly/blob/main/LICENSE)\n[![mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](https://github.com/python/mypy)\n[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://github.com/PyCQA/isort)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n## Introduction 🎉\nPlotly is great and powerful. But with great power comes great responsibility. And sometimes you just want to get a plot up and running as fast as possible. That\'s where blitzly ⚡️ comes in. It provides a set of functions that allow you to create plots with Plotly in a lightning-fast way. It\'s not meant to replace Plotly, but rather to complement it.\n\n## Install the package 📦\nIf you are using [pip](https://pip.pypa.io/en/stable/), you can install the package with the following command:\n```bash\npip install blitzly\n```\n\nIf you are using [Poetry](https://python-poetry.org/), you can install the package with the following command:\n```bash\npoetry add blitzly\n```\n## installing dependencies 🧑\u200d🔧\nWith [pip](https://pip.pypa.io/en/stable/):\n```bash\npip install -r requirements.txt\n```\n\nWith [Poetry](https://python-poetry.org/):\n```bash\npoetry install\n```\n## Available plots (so far 🚀)\n| Module | Method | Description |\n| ------ | ------ | ----------- |\n| [`bar`](https://invia-flights.github.io/blitzly/plots/bar/) | [`multi_chart`](https://invia-flights.github.io/blitzly/plots/bar/#blitzly.plots.bar.multi_chart) | Creates a bar chart with multiple groups. |\n| [`histogram`](https://invia-flights.github.io/blitzly/plots/histogram/) | [`simple_histogram`](https://invia-flights.github.io/blitzly/plots/histogram/#blitzly.plots.histogram.simple_histogram) | Plots a histogram with one ore more distributions. |\n| [`matrix`](https://invia-flights.github.io/blitzly/plots/matrix/) | [`binary_confusion_matrix`](https://invia-flights.github.io/blitzly/plots/matrix/#blitzly.plots.matrix.binary_confusion_matrix) | Plots a confusion matrix for binary classification data. |\n\n## Usage 🤌\nHere are some examples:\n[`multi_chart`](https://invia-flights.github.io/blitzly/plots/bar/#blitzly.plots.bar.multi_chart):\n```python\nfrom blitzly.bar import multi_chart\nimport numpy as np\n\ndata = np.array([[8, 3, 6], [9, 7, 5]])\nerror_array = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])\n\nmulti_chart(\n    data,\n    x_labels=["Vienna", "Berlin", "Lisbon"],\n    group_labels=["Personal rating", "Global rating"],\n    hover_texts=["foo", "bar", "blitzly"],\n    errors=error_array,\n    title="City ratings 🏙",\n    mark_x_labels=["Lisbon"],\n    write_html_path="see_the_blitz.html",\n)\n```\nGives you this:\n\n<img src="https://github.com/invia-flights/blitzly/raw/main/docs/assets/images/example_plots/city_rating.png" alt="city rating plot" width="1000" height="555"/>\n',
    'author': 'Prem Srinivasan',
    'author_email': 'prem.srinivasan@invia.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/invia-flights/blitzly',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
