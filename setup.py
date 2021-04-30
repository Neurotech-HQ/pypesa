from os import path
from setuptools import setup

# read the contents of your description file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'description.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="python-pesa",
    version="0.6",
    description='Python package for Vodacom Mpesa API Integration',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Kalebu/pypesa',
    download_url="https://github.com/Kalebu/pypesa/archive/0.4.tar.gz",
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["pypesa"],
    keywords=[
        "pypesa",
        "python-pesa",
        "mpesa python",
        "vodacom python",
        "pypesa package",
        "pypesa python package",
        "vodacom python package",
        "pypesa github",
        "python pypesa",
    ],

    install_requires=[
        'requests',
        'pycryptodome'
    ],

    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
