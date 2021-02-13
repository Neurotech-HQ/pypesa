from distutils.core import setup

setup(
    name="python-pesa",
    version="0.2",
    description='Python package for Vodacom Mpesa API Integration',
    url='https://github.com/Kalebu/pypesa',
    download_url="https://github.com/Kalebu/pypesa/archive/0.2.tar.gz",
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
