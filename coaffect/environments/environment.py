""" Create an Environment to hold an experiment, likely virtual.

Base Class:
    Environment

Subclasses:

"""

#: Dependencies
import numpy
import random

class Environment(object):
    """ Base class for Environment object.

    """

    def __init__(self, unique_id, name=''):
        """ Initialize an environment.

        Args:
            unique_id: unique integer identifier of the environment
            name: (optional) string identifier for convenient reference

        Attrs:
            _unique_id (int)
            _name (str)

        """
        self._unique_id = unique_id
        self._name = name

    def get_unique_id(self):
        """ Return unique_id.

        """
        return self._unique_id

    def get_name(self):
        """ Return name, if given, else pass.

        """
        return self._name if self._name else pass

    def step(self):
        """ Step method required for all environments. Override to use in
            practice.

        Requirements: Define in subclasses.

        """
        pass
