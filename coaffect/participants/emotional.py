""" Extend basic agent to an emotional agent.

"""

#: Dependencies
import numpy
import random

from .base import Agent

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
