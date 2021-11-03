"""Python package for Vodacom Mpesa API Integration.

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
