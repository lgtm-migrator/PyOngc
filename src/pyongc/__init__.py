"""Python interface to OpenNGC database data.

:license: MIT, see LICENSE for more details.
"""

from pkg_resources import resource_filename


__version__ = '0.7.0'
DBDATE = 20211113  # Version of database data

DBPATH = resource_filename(__name__, 'ongc.db')
