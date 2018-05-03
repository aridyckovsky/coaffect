""" Create an Environment to hold an experiment, likely virtual.

Base Class:
    Environment

Subclasses:

"""

#: Dependencies
import numpy
import random

from ..spaces.base import Space
from ..networks.base import Network

from ..utils.tracking_object import TrackingObject

class Environment(TrackingObject):
    """ Base class for Environment object.

    """

    def __init__(self, unique_id, space, network, name=''):
        """ Initialize an environment.

        Args:
            unique_id (int): unique integer identifier of the environment
            space (dict): config mapping of space features environment has
            network (dict): config mapping of network features environment has
            name: (optional) string identifier for convenient reference

        Attrs:
            _unique_id (int)
            _name (str)
            space (dict)
            network (dict)

        """
        super().__init__()
        self._unique_id = unique_id
        self._name = name

        self.space = Space(space)
        self.network = Network(network)

    def populate(self, agents):
        """ Populate an environment instance with list of agents.

        Args:
            agents(list): List of Agent objects

        """
        for agent in agents:
            self.network.populate(agents)


    def step(self):
        """ Step method required for all environments. Override to use in
            practice.

        Requirements: Define in subclasses.

        """
        pass

    #: Begin getters
    def get_id(self):
        """ Return unique_id.

        """
        return self._unique_id

    def get_space(self):
        return self._space

    def get_network(self):
        return self._network

    def get_name(self):
        """ Return name, if given, else pass.

        """
        return self._name if self._name else 'No Name'
