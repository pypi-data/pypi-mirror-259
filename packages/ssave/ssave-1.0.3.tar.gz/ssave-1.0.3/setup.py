from setuptools import setup, find_packages

def read_file(file):
   with open(file) as f:
        return f.read()
    
long_description = read_file("README.md")
version = 'v1.0.3'

setup(
    name = 'ssave',
    version = version,
    author = 'SCOS-Apps',
    author_email = 'hsc100zz@gmail.com',
    url = 'https://best-practice-and-impact.github.io/example-package-python/',
    description = 'SCOS Save Utility for Python3',
    long_description_content_type = "text/markdown",  # If this causes a warning, upgrade your setuptools package
    long_description = long_description,
)