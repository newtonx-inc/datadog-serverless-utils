from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(this_directory, "requirements.txt")) as f:
    install_requires = [line for line in map(str.strip, f.readlines()) if line and not line.startswith("#")]

setup(
    name='datadog-serverless-utils',
    version='1.0.2',
    url='https://github.com/newtonx-inc/datadog-serverless-utils',
    author='NewtonX',
    author_email='',
    python_requires='>=3.4',
    install_requires=install_requires,
    test_suite="tests.test_utils",
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=find_packages("src", exclude="tests"),
    description='Utilities for integration between serverless execution environments and DataDog',
)
