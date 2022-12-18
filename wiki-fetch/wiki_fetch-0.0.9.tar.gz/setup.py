# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wiki_fetch']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2']

entry_points = \
{'console_scripts': ['wiki-fetch = wiki_fetch.__main__:run']}

setup_kwargs = {
    'name': 'wiki-fetch',
    'version': '0.0.9',
    'description': 'Parser for Wikipedia.org',
    'long_description': '# wiki-fetch\n\n[![PyPI](https://img.shields.io/pypi/v/wiki-fetch)](https://github.com/d3z-the-dev/wiki-fetch/releases/)\n[![Status](https://img.shields.io/pypi/status/wiki-fetch)](https://pypi.org/project/wiki-fetch/)\n[![PyPI Downloads](https://img.shields.io/pypi/dm/wiki-fetch)](https://pypi.org/project/wiki-fetch/)\n[![Python Version](https://img.shields.io/pypi/pyversions/wiki-fetch?color=%23244E71)](https://pypi.org/project/wiki-fetch/)\n[![License](https://img.shields.io/pypi/l/wiki-fetch?color=272727)](https://en.wikipedia.org/wiki/Apache_License#Apache_License_2.0)\n[![Issues](https://img.shields.io/github/issues/d3z-the-dev/wiki-fetch)](https://github.com/d3z-the-dev/wiki-fetch/issues)\n\n## Installation\n\n- PyPI\n\n```bash\npip install wiki-fetch\n```\n\n- Source\n\n```bash\ngit clone git@github.com:d3z-the-dev/wiki-fetch.git\ncd wiki-fetch && poetry build\npip install ./dist/*.whl\n```\n\n## Usage\n\n### CLI\n\n| Option           | Flag | Long       | Default | Example                                   |\n| ---------------- | ---- | ---------- | ------- | ----------------------------------------- |\n| Wiki\'s page link | `-u` | `--url`    | None    | <https://en.wikipedia.org/wiki/The_Doors> |\n| Search query     | `-q` | `--query`  | None    | The Doors (band)                          |\n| Page language    | `-l` | `--lang`   | English | English                                   |\n| Part of the page | `-p` | `--part`   | all     | infobox                                   |\n| Parts by order   | `-i` | `--item`   | all     | first                                     |\n| Output format    | `-o` | `--output` | text    | text                                      |\n\n```bash\nwiki-fetch -q \'The Doors (band)\' -p infobox -i first\n```\n\n<details>\n<summary>output</summary>\n\n```yaml\nInfobox: \n    The Doors: \n        The Doors: \n            Image: https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/The_Doors_1968.JPG/250px-The_Doors_1968.JPG\n            Caption: The Doors in 1966: Morrison (left), Densmore (centre), Krieger (right) and Manzarek (seated)\n        Background information: \n            Origin: Los Angeles, California, U.S.\n            Genres: \n                Psychedelic Rock\n                Blues Rock\n                Acid Rock\n            Years active: \n                1965-1973\n                1978\n            Labels: \n                Elektra\n                Rhino\n            Spinoffs: \n                The Psychedelic Rangers\n                Butts Band\n                Nite City\n                Manzarek-Krieger\n            Spinoff of: Rick & the Ravens\n            Past members: \n                Jim Morrison\n                Ray Manzarek\n                Robby Krieger\n                John Densmore\n            Website: thedoors.com\nURL: https://en.wikipedia.org/?search=The Doors (Band)\n```\n</details>\n\n### Python\n\n| Argument | Values                                                         | Description                     |\n| -------- | -------------------------------------------------------------- | ------------------------------- |\n| url      | `str`                                                          | Any Wiki\'s page URL             |\n| query    | `str`                                                          | Any query string                |\n| lang     | `str`                                                          | Any of available languages      |\n| part     | `infobox`, `paragraph`, `table`, `list`, `thumb`, `toc`, `all` | Specify page part               |\n| item     | `first`, `last`, `all`                                         | Specify the order of the part   |\n\n```python\nfrom wiki_fetch.driver import Wiki\n\noutput = Wiki().search(query=\'The Doors (band)\', part=\'infobox\', item=\'first\')\nprint(output.json)\n```\n\n<details>\n<summary>output</summary>\n\n```json\n{\n    "Infobox": [\n        {\n            "The Doors": {\n                "The Doors": {\n                    "Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/The_Doors_1968.JPG/250px-The_Doors_1968.JPG",\n                    "Caption": "The Doors in 1966: Morrison (left), Densmore (centre), Krieger (right) and Manzarek (seated)"\n                },\n                "Background information": {\n                    "Origin": "Los Angeles, California, U.S.",\n                    "Genres": [\n                        "Psychedelic Rock",\n                        "Blues Rock",\n                        "Acid Rock"\n                    ],\n                    "Years active": [\n                        "1965-1973",\n                        "1978"\n                    ],\n                    "Labels": [\n                        "Elektra",\n                        "Rhino"\n                    ],\n                    "Spinoffs": [\n                        "The Psychedelic Rangers",\n                        "Butts Band",\n                        "Nite City",\n                        "Manzarek-Krieger"\n                    ],\n                    "Spinoff of": "Rick & the Ravens",\n                    "Past members": [\n                        "Jim Morrison",\n                        "Ray Manzarek",\n                        "Robby Krieger",\n                        "John Densmore"\n                    ],\n                    "Website": "thedoors.com"\n                }\n            }\n        }\n    ],\n    "URL": "https://en.wikipedia.org/?search=The Doors (Band)"\n}\n```\n</details>\n',
    'author': 'd3z',
    'author_email': 'd3z.the.dev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/d3z-the-dev/wiki-fetch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
