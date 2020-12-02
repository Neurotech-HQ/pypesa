from setuptools import setup

setup(
    name='pypesa',
    version='1.0.0',
    description='Python package for Vodacom Mpesa API Integration',
    url='https://github.com/Kalebu/pypesa',
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=['pypesa'],
    install_requires=[
        'requests',
    ],
    zip=False
)
