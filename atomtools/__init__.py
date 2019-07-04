"""
independent chemical symbols
"""


__version__ = '1.7.0'
def version():
    return __version__

from . import name, unit, geo
from . import file, string, system
from . import types
from .filetype import filetype
from .status import Status



