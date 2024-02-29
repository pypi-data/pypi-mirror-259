# setup.py

from setuptools import setup, find_packages

setup(
    name='simple-calculator-py',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={},
    description='A simple calculator package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Tanvir-yzu',
    author_email='2020tanvir1971@gmail.com',
    url='https://github.com/Tanvir-yzu/simplecalculator.git',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
