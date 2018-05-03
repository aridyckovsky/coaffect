""" 1-Dimensional Space for an environment.

"""

from .base import Space

class Space1D(Space):
    """ 1D Space.

    """
    def __init__(self, left, right):
        """ Initialize 1-dimensional space with left and right limits.

        Args:
            left (int)
            right (int)

        """
        super().__init__([(left, right)])
        self._left = left
        self._right = right
