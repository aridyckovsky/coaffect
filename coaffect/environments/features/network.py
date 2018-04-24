""" Say something about network class.

Base Class:
    Network

"""

#: Dependencies
import networkx as nx
import numpy as np
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

    def populate(self, agents=[], groups=[]):
        """ Populate a network with nodes, such as agents and groups.

        Args:
            agents (list)
            groups (list)

        """
        if agents:
            for agent in agents:
                pass
        if groups:
            for group in groups:
                pass

    def connect(self, ties):
        """ Connect nodes of the network.

        Args:
            ties (list): List of networkx-appropriate edges

        """
        for tie in ties:
            pass

    #: Begin getters
    def get_unique_id(self):
        return self._unique_id

    def get_graph(self, options):
        """ Return the graph of a network. (Use options to return graph in
            particular object type.)

        Args:
            options (dict)

        """
        return self._graph

    def get_agents(self):
        #: TODO specify agent nodes
        return self._graph.nodes()

    def get_groups(self):
        #: TODO specify group nodes
        return self._graph.nodes()

    def get_ties(self):
        return self._graph.edges()
