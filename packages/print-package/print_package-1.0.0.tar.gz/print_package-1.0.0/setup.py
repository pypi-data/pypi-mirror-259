# setup.py

from setuptools import setup, find_packages

setup(
    name='print_package',
    version='1.0.0',
    packages=find_packages(),
    author='Tanvir',
    author_email='2020tanvir1971@gmail.com',
    description='A simple Python package for printing messages.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Tanvir-yzu/print_package.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
