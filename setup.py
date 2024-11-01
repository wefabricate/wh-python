# coding: utf-8

"""
    Weheat Backend

    This is the backend for the Weheat project

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501
import pathlib

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "weheat"
VERSION = "2024.11.2"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum"
]

setup(
    name=NAME,
    version=VERSION,
    description="Weheat Backend client",
    author="Jesper Raemaekers",
    author_email="jesper.raemaekers@wefabricate.com",
    url="https://github.com/wefabricate/wh-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Weheat Backend"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=pathlib.Path("README.md").read_text(),  # noqa: E501
    package_data={"weheat": ["py.typed"]},
    license="MIT",
    license_files = ('LICENSE',),
)
