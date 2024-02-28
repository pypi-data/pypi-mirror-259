# -*- coding: utf-8 -*-
"""
This module contains the tool of sample
"""
import os
from setuptools import setup, find_namespace_packages
from datetime import datetime
from packaging import version


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


base_version = '0.5.1'


def get_version():
    v = version.parse(base_version)

    if os.getenv("GITHUB_REF_TYPE") == "tag":
        if gh_ref := os.getenv("GITHUB_REF_NAME"):
            if "-pre" in gh_ref:
                import re
                match = re.search(pattern=r".+-pre(\d+).*", string=gh_ref)
                if match:
                    pre_number = match.group(1)
                    return v.base_version + ".rc" + pre_number
            else:
                return v.base_version

    if v.is_devrelease:
        dev_number = datetime.utcnow().strftime("%Y%m%d%H%M")
        return v.base_version + "dev" + dev_number

    return base_version


long_description = (
    read('README.rst')
)


setup(name='nexiles.tools.api',
      version=get_version(),
      description="nexiles.tools.api -- python nexiles Windchill gateway http client api",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='',
      author='Stefan Eletzhofer',
      author_email='stefan.eletzhofer@nexiles.com',
      url='http://nexiles.github.io/nexiles.tools.api/',
      license='BSD',
      packages=find_namespace_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'requests',
                        'argparse',
                        'tabulate',
                        # -*- Extra requirements: -*-
                        ],
      entry_points={
          'console_scripts': [
              'nxtools = nexiles.tools.api.main:main',
          ]
      }
      )
