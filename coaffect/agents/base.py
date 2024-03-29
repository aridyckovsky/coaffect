""" Create an Agent as a participant for experiment(s).

Abstract Base Class:
    Agent

Concrete Extended Class(es):
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
        """ Extended subclass of Agent for an emotional agent for use in
            real and virtual experiments.

        Args:

        Attrs:

        """
        super().__init__(unique_id, experiment)

    def perceive(self, situation):
        """ Perceive a situation in the surrounding environment, including
            social and spatial factors.

        Args:
            situation

        """
        try:
            self._set_state(situation)
        except ValueError:
            raise ValueError('Uh Oh!')
        else:
            pass

    def express(self):
        curr = self.get_state()
        return curr
