from movie import Movie
from person import Person

VERSION = (0, 4, 1)
__version__ = '.'.join(map(str, VERSION))

__all__ = ['Movie', 'Person']
