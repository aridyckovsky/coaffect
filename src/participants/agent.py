""" Create an Agent as a participant for experiment(s).

Core Object(s):
    Agent

"""

#: Dependencies
import numpy
import random

class Agent(object):
    """ Base class for Agent object.

    """

    def __init__(self, _id, experiment):
        """ Initialize an agent with unique id.

        Args:
            _id: unique integer identifier
            experiment: reference to experiment agent is a participant in

        """
        self._id = _id
        super().__init__(_id, experiment)

    def step(self):
        """ Step method required for all agents. Override to use in
            practice.

        """
        pass
