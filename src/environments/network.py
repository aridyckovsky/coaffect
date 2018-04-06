""" Say something about network class.

Core Object(s):
    Network

"""

#: Dependencies
import networkx
import numpy
import random

class Network(object):
    """ Base class for Network.

    """

    def __init__(self, _id, experiment):
        """ Initialize a NetworkX network of participant objects.

        Args:
            _id: unique integer identifier for the network
            experiment: reference to experiment network is a participant in

        """
        super().__init__(_id, experiment)
        self._id = _id
        self.graph = nx.DiGraph() # network structure
