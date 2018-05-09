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

    def __init__(self, unique_id, experiment, space, network, name=''):
        """ Initialize an environment.

        Args:
            unique_id (int): unique integer identifier of the environment
            space (dict): config mapping of space features environment has
            network (dict): config mapping of network features environment has
            name: (optional) string identifier for convenient reference

        Attrs:
            __unique_id (str)
            __name (str)
            space (dict)
            network (dict)

        """
        super().__init__()
        self.__unique_id = unique_id
        self.__name = name
        self.experiment = experiment

        self.agents = {}
        self.groups = {}

        self.space = Space(space)
        self.network = Network(network)

    def add_agents(self, agents):
        """ Populate an environment instance with list of agents.

        Args:
            agents (list): List of Agent objects

        """
        for agent in agents:
            agent_id = agent.get_unique_id()
            self.agents[agent_id] = agent
            self.network.add_agent(agent)

    def add_groups(self, groups):
        """ Populate an environment instance with list of groups.

        Args:
            groups (list): List of Group objects

        """
        for group in groups:
            group_id = group.get_unique_id()
            self.groups[group_id] = group
            self.network.add_group(groups)

    def update(self):
        """ Update method required for environments. Subclasses may (and should)
            specialize and extend as necessary. Records current measures to
            experiment's history.

        """
        self.experiment.record(self.get_measures())

    #: Begin getters
    def get_unique_id(self):
        """ Return unique_id.

        """
        return self.__unique_id

    def get_name(self):
        """ Return name, if given, else pass.

        """
        return self.__name if self.__name else 'No Name'

    def get_space(self):
        return self._space

    def get_network(self):
        return self._network
