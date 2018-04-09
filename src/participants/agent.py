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
        #super().__init__(_id, experiment) #TODO: is this right?
        self._id = _id
        self._state = [] # TODO put actual empty state here...maybe vector? maybe dict?

    def get_id(self):
        """ Get agent's unique identifier.

        """
        return self._id

    def get_state(self):
        """ Get agent's current state.

        """
        return self._state

    def step(self):
        """ Step method required for all agents. Override to use in
            practice with specific schedules/experiments.

        """
        pass
