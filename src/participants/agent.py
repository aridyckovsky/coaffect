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

    def __init__(self, unique_id, experiment):
        """ Initialize an agent with unique id.

        Args:
            unique_id: unique integer identifier
            experiment: reference to experiment instance

        Attrs:
            _unique_id (int)
            _experiment (dict)
            _state (dict) ... or?

        """
        self._unique_id = unique_id
        self._experiment = experiment
        self._state = [] # TODO put actual empty "state" here...maybe vector? maybe dict?

    def get_id(self):
        """ Get agent's unique identifier.

        """
        return self.unique_id

    def get_experiment(self):
        """ Get agent's experiment information, if available.

        """
        return self._experiment

    def get_state(self):
        """ Get agent's current state.

        """
        return self._state

    def _set_state(self):
        """ Set agent's current state. Limited to access by subclasses,
            not public method.

        Requirements: Define in subclasses.

        """
        pass

    def step(self):
        """ Step method required for all agents.

        Requirements: Define in subclasses.

        """
        pass

class EmotionalAgent(Agent):
    """ Create emotional agent by extending and overriding base class Agent.

    """

    def __init__(self, unique_id, experiment):
        super().__init__(unique_id, experiment)
