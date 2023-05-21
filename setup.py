"""
Geometrify package setup file.

This file imports the necessary setup function from setuptools module, reads
the content of Readme.rst file and passes it as long description, 
and defines package name, version, description, author, author email, url, packages, 
package data, keywords, classifiers, and requirements.

For more information about the package, please visit https://github.com/1abhi6/Geometrify.
"""

from setuptools import setup
import setuptools

with open("Readme.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

SHORT_DESCRIPTION = """Geometrify is a Python package for easy creation, manipulation,
                        and analysis of 2D geometries.
                    """

setup(
    name="Geometrify",
    version="1.0.5",
    description=SHORT_DESCRIPTION,
    author="Abhishek Santosh Gupta",
    author_email="abhi@getifyme.com",
    url="https://github.com/1abhi6/Geometrify",
    long_description=long_description,
    packages=setuptools.find_packages(),
    include_package_data=True,
    license="MIT",
    keywords=["2D geometry", "Coordinate geometry", "Coordinate datatype"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
)
