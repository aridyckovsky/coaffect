""" Say something about network class.

Base Class:
    Network

"""

#: Dependencies
import networkx
import numpy
import random

class Network(object):
    """ Base class for Network.

    """

    def __init__(self, unique_id):
        """ Initialize a NetworkX network of participant objects.

        Args:
            _id: unique integer identifier for the network

        """
        self._unique_id = unique_id
        self._graph = nx.DiGraph() # network structure

    def get_id(self):
        return self._unique_id

    def get_graph(self, options):
        """ Return the graph of a network. Use options to return graph in
            particular object type.

        """
        if options:
            pass
        else:
            return self._graph
