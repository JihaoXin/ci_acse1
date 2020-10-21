from .functions1 import my_sum, factorial
from .constants import pi
from .print import myprint
from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
