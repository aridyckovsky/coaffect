""" Create a SpatialAgent as a participant for experiment(s).

"""

from .base_agent import Agent

class SpatialAgent(Agent):

    """ Create a spatially aware agent by extending and overriding base class Agent.

    """

    #: Default measure names
    POSITION = 'position'

    #: Default measures and type
    SPATIAL_MEASURES = {
        POSITION: ()
    }

    def __init__(self, unique_id, measures={}):
        """ Extended subclass of Agent for a spatially aware agent for use in
            real and virtual experiments.

        Args:

        Attrs:

        """

        #: Update argument to have required measures for an EmotionalAgent
        measures.update(self.SPATIAL_MEASURES)

        #: Inherit from parent Agent, including updated measures
        super().__init__(unique_id, measures)

    """

    BEGIN GETTERS

    """

    def get_position(self):
        """ Get position measure.

        """
        return self.get_measure(self.POSITION)
