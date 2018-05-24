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

from ..utils.trackable_object import TrackableObject
from ..utils.state import State

class Agent(TrackableObject):
    """ Base class for Agent object.

    """

    BASE_MEASURES = {}

    def __init__(self, unique_id, measures={}):
        """ Initialize an agent with unique id and experiment agent is part of.

        Args:
            unique_id: unique integer identifier
            experiment: reference to experiment instance
            measures: dict mapping string labels to data types

        Attrs:
            __unique_id (int)
            __state (dict, as defined in State)
            experiment (dict)

        """
        super().__init__()

        self._unique_id = unique_id

        measures.update(self.BASE_MEASURES)
        self.__state = State(measures)

    def __repr__(self):
        return 'Agent({})'.format(self._unique_id)

    def __eq__(self, other):
        #TODO must be same class!!!
        return self.get_unique_id() == other.get_unique_id()

    def update(self):
        """ Update method required for all agents. Subclasses may (and should)
            specialize and extend as necessary. Records current measures to
            experiment's history.

        """
        # TODO
        pass

    """

    BEGIN GETTERS

    """

    def get_unique_id(self):
        """ Get agent's unique identifier.

        """
        return self._unique_id

    def get_state(self):
        """ Get agent's current state be accessing State's
            `get_measures` method.

        """
        return self.__state

    def get_measures(self):
        """ Return measures in state.

        """
        return self.get_state().get_measures()

    def get_measure(self, measure_name):
        """ Get a measure by name.

        """
        return self.get_state().get_measure(measure_name)

    def get_position(self):
        """ Get position of agent.

        """
        return self.get_measure(self.POSITION)
