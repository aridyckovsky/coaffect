""" Say something about network class.

Base Class:
    Network

"""

#: Dependencies
import networkx as nx
import numpy as np
import random

from ..utils.tracking_object import TrackingObject

class Network(TrackingObject):
    """ Base class for Network, a representation of agents and groups
        as nodes and edges in an environment.

    """

    AGENT_NODE_TYPE = 'agent'
    GROUP_NODE_TYPE = 'group'
    SOCIAL_TIE_EDGE_TYPE = 'social_tie'
    IDENTIFICATION_EDGE_TYPE = 'identification'

    def __init__(self, unique_id):
        """ Initialize an empty NetworkX DiGraph.

        Args:
            unique_id: unique str identifier for the network

        """
        super().__init__()
        self._unique_id = unique_id
        self._graph = nx.DiGraph() # network structure

    def add_agents(self, agents):
        """ Populate graph with nodes representing agents by unique_ids.

        Args:
            agents (list): list of string identifiers for agents

        """
        self._graph.add_nodes_from(agents, node_type=AGENT_NODE_TYPE)

    def remove_agents(self, agents):
        """ Remove nodes representing agents from graph by unique_ids

        Args:
            agents (list): list of string identifiers

        """
        self._graph.remove_nodes_from(agents)

    def add_groups(self, groups):
        """ Populate graph with nodes representing groups.

        Args:
            groups (list): list of string identifiers

        """
        self._graph.add_nodes_from(groups, node_type=GROUP_NODE_TYPE)

    def remove_groups(self, groups):
        """ Remove nodes representing groups from graph by unique_ids

        Args:
            groups (list): list of string identifiers

        """
        self._graph.remove_nodes_from(groups)

    def add_social_ties(self, social_ties):
        """ Connect agent nodes with directed edges in the graph.

        Args:
            social_ties

        """
        self._graph.add_edges_from(social_ties, edge_type=SOCIAL_TIE_EDGE_TYPE)

    def remove_social_ties(self, social_ties):
        """ Remove directed edges between agent nodes.

        Args:
            social_ties

        """
        self._graph.remove_edges_from(social_ties)

    def add_social_ties(self, social_ties):
        """ Connect agent nodes with directed edges in the graph.

        Args:
            social_ties

        """
        self._graph.add_edges_from(social_ties, edge_type=SOCIAL_TIE_EDGE_TYPE)

    def remove_social_ties(self, identifications):
        """ Remove directed edges between group nodes.

        Args:
            identifications

        """
        self._graph.remove_edges_from(identifications)

    """

    BEGIN GETTERS

    """

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
