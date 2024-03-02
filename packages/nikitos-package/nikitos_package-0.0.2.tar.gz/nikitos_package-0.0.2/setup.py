from setuptools import setup, find_packages
setup(
name='nikitos_package',
version='0.0.2',
author='Nikita Romm',
author_email='nikitaromm@gmail.com',
description='This is a test package',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)