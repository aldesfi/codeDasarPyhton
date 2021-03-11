import io
import os.path
from setuptools import setup

VERSION_PATH = os.path.join(
    os.path.dirname(__file__), 'helloword/VERSION.txt')
with io.open(VERSION_PATH, 'r', encoding='utf-8') as f:
  version = f.read().strip()

setup(
    name = "helloword",        
    version = version,
    packages=["helloword"],   
                               
    dependency_links = [],      
    install_requires=[],
    extras_require={},     
                          
    package_data = {"helloword": ["VERSION.txt"]},
    author="Mak Jono",
    author_email = "alldes182@gmail.com",
    description = "Contoh Code Dasar Pada Pyhton",
    license = "Apache 2.0",
    keywords= "example documentation tutorial",
    url = "http://github.com/aldesfi/codeDasarPyhton",
    entry_points = {
        "console_scripts": [        
            "codeDasarPyhton = helloword.main:main",
        ],
    }
)
