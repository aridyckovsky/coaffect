""" Create an EmotionalAgent as a participant for experiment(s).

"""

from .base import Agent

class EmotionalAgent(Agent):
    """ Create emotional agent by extending and overriding base class Agent.

    """

    #: Default measure names
    AROUSAL = 'arousal'

    #: Default measures by name and value type
    EMOTION_MEASURES = {
        AROUSAL: 0
    }

    def __init__(self, unique_id, experiment, measures={}):
        """ Extended subclass of Agent for an emotional agent for use in
            real and virtual experiments.

        Args:

        Attrs:

        """

        #: Update argument to have required measures for an EmotionalAgent
        measures.update(self.EMOTION_MEASURES)

        #: Inherit from parent Agent, including updated measures
        super().__init__(unique_id, experiment, measures)

        self.__memory = []

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
        pass

    def express(self):
        curr_arousal = self.get_arousal()
        pass

    def step(self, resolution, situation=None):
        """ Step updates an emotional agent by perceiving a situation,
            then updating the agent's state and relevant measures.

        Args:
            resolution (int): resolution as defined in a schedule
            situation

        """
        perception = self.perceive(situation)
        pass

    """

    BEGIN GETTERS

    """

    def get_arousal(self):
        """ Get arousal measure.

        """
        return self.get_measure(self.AROUSAL)

    def get_memory(self):
        """ Get memory of agent.

        """
        return self.__memory
