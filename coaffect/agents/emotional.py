""" Create an EmotionalAgent as a participant for experiment(s).

"""

from .base import Agent

class EmotionalAgent(Agent):
    """ Create emotional agent by extending and overriding base class Agent.

    """

    def __init__(self, unique_id, experiment, measures={}):
        """ Extended subclass of Agent for an emotional agent for use in
            real and virtual experiments.

        Args:

        Attrs:

        """

        #: Update argument to have required measures for an EmotionalAgent
        measures.update({
            'arousal': 0
        })

        #: Inherit from Agent, including updated measures
        super().__init__(unique_id, experiment, measures)

        self._memory = []

    def perceive(self, resolution, situation):
        """ Perceive a situation in the surrounding environment, including
            social and spatial factors.

        Args:
            situation (dict)

        Returns:
            perception (list): List of single dict mappings

        """
        perception = {}
        state = self.get_state()
        for feature, value in state:
            #TODO do something to a situation that returns a perception value
            perception[feature] = value

    def express(self):
        return self.get_state()['arousal']

    def step(self, resolution, situation=None):
        """ Step updates an emotional agent by perceiving a situation,
            then updating the agent's state and relevant measures.

        Args:
            resolution (int): resolution as defined in a schedule
            situation

        """
        perception = self.perceive(situation)
        for feature, value in perception:
            measure = {feature: value + self.get_feature(feature)}
            self._set_state(measure)