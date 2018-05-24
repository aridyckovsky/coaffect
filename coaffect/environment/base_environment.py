""" Create an Environment to hold an experiment, likely virtual.

Base Class:
    Environment

Subclasses:

"""

#: Dependencies
import numpy
import random

from ..space.base_space import Space
from ..network.base_network import Network

from ..utils.trackable_object import TrackableObject

class Environment(TrackableObject):
    """ Base class for Environment object.

    """

    AGENTS = 'agents'
    GROUPS = 'groups'

    def __init__(self, unique_id, space, network, name=''):
        """ Initialize an environment.

        Args:
            unique_id (int): unique integer identifier of the environment
            space (dict): config mapping of space features environment has
            network (dict): config mapping of network features environment has
            name: (optional) string identifier for convenient reference

        Attrs:
            _unique_id (str)
            _name (str)
            space (dict)
            network (dict)

        """
        super().__init__()
        self._unique_id = unique_id
        self._name = name

        self._agents = {}
        self._groups = {}

        self._space = Space(space)
        self._network = Network(network)

    def __repr__(self):
        return 'Environment({})'.format(self.get_unique_id())

    def __eq__(self, other):
        return self.get_unique_id() == other.get_unique_id()

    def add_agents(self, agents):
        """ Populate an environment instance with list of agents.

        Args:
            agents (list): List of Agent objects

        """
        for a in agents:
            a_id = agent.get_unique_id()
            self.agents[a_id] = a
            self.network.add_agent(a)

    def add_groups(self, groups):
        """ Populate an environment instance with list of groups.

        Args:
            groups (list): List of Group objects

        """
        for g in groups:
            g_id = g.get_unique_id()
            self._groups[g_id] = g
            self._network.add_group(g)

    def update(self):
        """ Update method required for environments. Subclasses may (and should)
            specialize and extend as necessary. Records current measures to
            experiment's history.

        """
        #self._experiment.record(self.get_measures())
        # do stuff, then return
        """

        Probably: for each thing, record(thing.get_measures()) by id

        """
        return {
            self.AGENTS: self.get_agents(),
            self.GROUPS: self.get_groups()
        }

    """

    BEGIN GETTERS

    """

    def get_unique_id(self):
        """ Return unique_id.

        """
        return self._unique_id

    def get_name(self):
        """ Return name, if given, else pass.

        """
        return self._name if self._name else 'No Name'

    def get_space(self):
        return self._space

    def get_network(self):
        return self._network

    def get_agents(self):
        return self._agents

    def get_groups(self):
        return self._groups
