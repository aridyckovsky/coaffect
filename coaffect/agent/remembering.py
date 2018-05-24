""" Create a RememberingAgent as a participant for experiment(s).

"""

from .base_agent import Agent

class RememberingAgent(Agent):
    """ Create an agent with memory by extending and overriding base class Agent.

    """

    #: Default measure names
    MEMORY = 'memory'

    #: Default measures and type
    REMEMBERING_MEASURES = {
        MEMORY: []
    }

    def __init__(self, unique_id, measures={}):
        """ Extended subclass of Agent for an emotional agent for use in
            real and virtual experiments.

        Args:

        Attrs:

        """

        #: Update argument to have required measures for an EmotionalAgent
        measures.update(self.REMEMBERING_MEASURES)

        #: Inherit from parent Agent, including updated measures
        super().__init__(unique_id, measures)

    """

    BEGIN GETTERS

    """

    def get_memory(self):
        """ Get memory measure.

        """
        return self.get_measure(self.MEMORY)
