""" Say something about Space class.

Base Class:
    Space

"""

#: Dependencies
import numpy
import random

# TODO: import a constant? from a defualts folder? or utils? hm...

class Space(object):
    """ Base class for Space.

    """

    def __init__(self, domain=[(0.,0.)]):
        """ Initialize Space.

        Args:
            domain: list of domain ranges given as tuple pairs of floats

        """
        self._domain = domain
        #TODO: Implement iterator to use next() and run schedules

    def get_domain(self, axis=None):
        if axis:
            try:
                 return self._domain[axis]
            except TypeError:
                print("Not a valid axis!")
                raise
        else:
            return self._domain

    def set_domain(self, new_domain):
        """ Set a completely new domain.

        """
        self._domain = domain

    def set_domain_axis(self, axis, new_axis_domain):
        """ Set a domain's axis.

        """
        #: TODO if axis exists, reset with new_axis_domain
        #:      else create new access with new_axis_domain
        pass
