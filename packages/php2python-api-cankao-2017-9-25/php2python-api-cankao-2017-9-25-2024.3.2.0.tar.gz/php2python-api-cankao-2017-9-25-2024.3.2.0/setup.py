#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import Php2pythonApiCankao2017925
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('Php2pythonApiCankao2017925'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="php2python-api-cankao-2017-9-25",
    version=Php2pythonApiCankao2017925.__version__,
    url="https://github.com/apachecn/php2python-api-cankao-2017-9-25",
    author=Php2pythonApiCankao2017925.__author__,
    author_email=Php2pythonApiCankao2017925.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Documentation",
        "Topic :: Documentation",
    ],
    description="PHP2Python API 参考 2017.9.25",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "php2python-api-cankao-2017-9-25=Php2pythonApiCankao2017925.__main__:main",
            "Php2pythonApiCankao2017925=Php2pythonApiCankao2017925.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
