""" Create an EmotionalGroup as a participant for experiment(s).

"""

from .base_group import Group

class EmotionalGroup(Group):
    """ Create emotional agent by extending and overriding base class Agent.

    """

    #: Default measure names
    AROUSAL = 'collective_arousal'

    #: Default measures by name and value type
    EMOTIONAL_MEASURES = {
        AROUSAL: 0.0
    }

    def __init__(self, unique_id, experiment, measures={}):
        """ Extended subclass of Agent for an emotional agent for use in
            real and virtual experiments.

        Args:

        Attrs:

        """

        #: Update argument to have required measures for an EmotionalAgent
        measures.update(self.EMOTIONAL_MEASURES)

        #: Inherit from parent Agent, including updated measures
        super().__init__(unique_id, experiment, measures)

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
