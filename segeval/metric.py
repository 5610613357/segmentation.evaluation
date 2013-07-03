'''
General metric utilities and constants.

.. moduleauthor:: Chris Fournier <chris.m.fournier@gmail.com>
'''
from .format import BoundaryFormat


METRIC_DEFAULTS = {
    'boundary_format': BoundaryFormat.mass,
    'permuted': False,
    'one_minus': False,
    'return_parts': False
}
