#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import MathematicsForComputerScienceMit6042j
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('MathematicsForComputerScienceMit6042j'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="mathematics-for-computer-science-mit-6-042j",
    version=MathematicsForComputerScienceMit6042j.__version__,
    url="https://github.com/apachecn/mathematics-for-computer-science-mit-6-042j",
    author=MathematicsForComputerScienceMit6042j.__author__,
    author_email=MathematicsForComputerScienceMit6042j.__email__,
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
    description="Mathematics for Computer Science (MIT 6.042J)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "mathematics-for-computer-science-mit-6-042j=MathematicsForComputerScienceMit6042j.__main__:main",
            "MathematicsForComputerScienceMit6042j=MathematicsForComputerScienceMit6042j.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
