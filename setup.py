from setuptools import setup, find_packages
import re

with open("tenkin/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="Tenkin",
    version=version,
    author="Luan Viana",
    packages= find_packages(),
    install_requires=[
        "click>=5.1",
    ],
)