""" Create an Agent as a participant for experiment(s).

Base Class:
    Agent

Subclass(es):
    EmotionalAgent

NOTES:
    - Simulation: One police officer will visit a street with fruit stand owners
        for two weeks (14 days = 14 opportunities to steal), come for 1 hour,
        during 1 hour, can steal fruit from a single fruit stand during that hour,
        at any point in that hour
    - Habituation: decrease "effective baseline" of arousal over course of days
    - Regulation: up- and down-regulation based on habituation and agent's
        rated ability to regulate, as well as social "help" to regulate from others

"""

#: Dependencies
import numpy
import random

from ..states.base import State

class Agent(object):
    """ Base class for Agent object.

    """

    def __init__(self, unique_id, experiment, measures={}):
        """ Initialize an agent with unique id and experiment agent is part of.

        Args:
            unique_id: unique integer identifier
            experiment: reference to experiment instance
            measures: dict mapping string labels to data types

        Attrs:
            _unique_id (int)
            _experiment (dict)
            _state (dict, as defined in State)

        """
        self._unique_id = unique_id
        self._experiment = experiment
        self._state = State(measures)

    def get_unique_id(self):
        """ Get agent's unique identifier.

        """
        return self.unique_id

    def get_experiment(self):
        """ Get agent's experiment information, if available.

        """
        return self._experiment

    def get_state(self):
        """ Get agent's current state be accessing State's
            `get_measures` method.

        """
        return self._state.get_measures()

    def get_feature(self, feature):
        return self.get_state()[feature]

    def _set_state(self, measure):
        """ Set agent's current state. Limited to access by subclasses,
            not public method.

        Args:
            measure (dict): Single measure to update (e.g., {'arousal': 0})

        """
        self._state._set_measures(measure)

    def step(self):
        """ Step method required for all agents.

        Requirements: Define in subclasses.

        """
        pass
