from setuptools import setup
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="Geometrify",
    version="0.0.1",
    description="Geometrify is a Python package for easy creation, manipulation, and analysis of 2D geometries, providing comprehensive tools for various operations",
    author="Abhishek Santosh Gupta",
    author_email="abhi@getifyme.com",
    url="https://github.com/1abhi6/Geometrify",
    long_description=long_description,
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
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
