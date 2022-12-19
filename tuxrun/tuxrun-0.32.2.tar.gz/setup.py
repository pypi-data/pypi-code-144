#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['tuxrun', 'tuxrun.devices', 'tuxrun.templates', 'tuxrun.tests']

package_data = \
{'': ['*'],
 'tuxrun.templates': ['devices/*',
                      'dispatchers/*',
                      'jobs/*',
                      'tests/*',
                      'wrappers/*']}

install_requires = \
['jinja2', 'requests', 'PyYAML']

entry_points = \
{'console_scripts': ['tuxrun = tuxrun.__main__:main']}

setup(name='tuxrun',
      version='0.32.2',
      description='Command line tool for testing Linux under QEMU',
      author='Antonio Terceiro',
      author_email='antonio.terceiro@linaro.org',
      url='https://tuxsuite.com/',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      entry_points=entry_points,
      python_requires='>=3.6',
     )
