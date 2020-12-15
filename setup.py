from setuptools import setup, find_packages
import re

with open("tenkin/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="Tenkin",
    version=version,
    author="Luan Viana",
    packages=find_packages(),
    package_data={'': [
        './static/html/index.html',
        './static/css/style.css',
        './static/js/main.js',
        './static/js/service-worker.js',
        './static/json/manifest.json',
        './static/python/main.py',
        './static/assets/favicon.ico',
        './static/assets/logo192.png',
        './static/assets/logo512.png',
        ]
    },
    include_package_data=True,
    install_requires=[
        "click>=5.1",
        "uvicorn>=0.13.1",
        "beautifulsoup4>=4.9.3",
    ],
)