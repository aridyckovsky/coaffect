""" Default Space class to define an environment's spatial physics.

Base Class:
    Space

"""

#: Dependencies
import numpy
import random

from ..utils.trackable_object import TrackableObject

class Space(TrackableObject):
    """ Base class for Space.

    """

    def __init__(self, domain=[]):
        """ Initialize Space.

        Args:
            domain: list of domain ranges given as tuple pairs of floats

        """
        super().__init__()
        self.__domain = domain
        #TODO: Implement iterator to use next() and run schedules

    def __repr__(self):
        return 'Space({})'.format(self.__domain)

    def get_domain(self, axis=None):
        if axis:
            try:
                 return self.__domain[axis]
            except TypeError:
                print("Not a valid axis!")
                raise
        else:
            return self.__domain

    def set_domain(self, new_domain):
        """ Set a completely new domain.

        """
        self.__domain = domain

    def set_domain_axis(self, axis, new_axis_domain):
        """ Set a domain's axis.

        """
        #: TODO if axis exists, reset with new_axis_domain
        #:      else create new access with new_axis_domain
        pass
