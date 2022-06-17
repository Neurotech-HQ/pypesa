"""
pypesa: A Python wrapper on Mpesa public API for mobile payments Integration.
=============================================================================

Documentation is available in the docstrings
and online at http://kalebu.github.io/pypesa

Contents
--------
pypesa contents goes here!

Subpackages
-----------
Using any of the pypesa subpackages requires either
an explicit or implicit import. For example,
``import pypesa`` | ``import pypesa.mpesa`` | ``from pypesa import Mpesa``.

::

 mpesa                    --- Mpesa class
 mpesa_exceptions         --- Exception classes
 service_urls             --- Services urls


Utility tools
-------------
::

 tests                    --- Run pypesa unittests

Changelog
---------
**Version 0.4** - 2021 April 30    
    Improved auth decorator with wraps
    Added example in methods docstring to ease the usage

**Version 0.3** - 2021 February 14
    Fixed Query transaction status bug
    Improved docstring documentation
    Added json response to debit creation and payments

**Version 0.2** - 2021 February 13
    Fixed bug | added doc string | changed import format

**Version 0.1** - 2021 February 12
    Initial release.

"""

__version__ = '0.4'
__all__ = ['Mpesa',]

from pypesa.mpesa import Mpesa
