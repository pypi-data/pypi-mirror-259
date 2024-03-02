#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import MiningMassiveDataSetsReadingMaterialStanfordCs246
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('MiningMassiveDataSetsReadingMaterialStanfordCs246'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="mining-massive-data-sets-reading-material-stanford-cs246",
    version=MiningMassiveDataSetsReadingMaterialStanfordCs246.__version__,
    url="https://github.com/apachecn/mining-massive-data-sets-reading-material-stanford-cs246",
    author=MiningMassiveDataSetsReadingMaterialStanfordCs246.__author__,
    author_email=MiningMassiveDataSetsReadingMaterialStanfordCs246.__email__,
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
    description="Mining Massive Data Sets Reading Material (Stanford CS246)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "mining-massive-data-sets-reading-material-stanford-cs246=MiningMassiveDataSetsReadingMaterialStanfordCs246.__main__:main",
            "MiningMassiveDataSetsReadingMaterialStanfordCs246=MiningMassiveDataSetsReadingMaterialStanfordCs246.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
