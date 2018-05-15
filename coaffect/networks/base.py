""" Say something about network class.

Base Class:
    Network

"""

#: Dependencies
import networkx as nx
import numpy as np
import random

from ..utils.tracking_object import TrackingObject
from ..utils.state import State

class Network(TrackingObject):
    """ Base class for Network, a representation of agents and groups
        as nodes and edges in an environment.

    """

    AGENT_NODE_TYPE = 'agent'
    GROUP_NODE_TYPE = 'group'
    SOCIAL_TIE_EDGE_TYPE = 'social_tie'
    IDENTIFICATION_EDGE_TYPE = 'identification'

    #: Default names of measures required in all networks
    DENSITY = 'density'

    #: Default state measures
    BASE_MEASURES = {
        DENSITY: 0
    }

    def __init__(self, unique_id, measures={}):
        """ Initialize an empty NetworkX DiGraph.

        Args:
            unique_id: unique str identifier for the network

        """
        super().__init__()
        self.__unique_id = unique_id
        self.__graph = nx.DiGraph() # network structure

        measures.update(self.BASE_MEASURES)
        self.__state = State(measures)

    def __repr__(self):
        return 'Network({})'.format(self.__unique_id)

    def add_agents(self, agents):
        """ Populate graph with nodes representing agents by unique_ids.

        Args:
            agents (list): list of string identifiers for agents

        """
        self.__graph.add_nodes_from(agents, node_type=self.AGENT_NODE_TYPE)

    def remove_agents(self, agents):
        """ Remove nodes representing agents from graph by unique_ids

        Args:
            agents (list): list of string identifiers

        """
        self.__graph.remove_nodes_from(agents)

    def add_groups(self, groups):
        """ Populate graph with nodes representing groups.

        Args:
            groups (list): list of string identifiers

        """
        self.__graph.add_nodes_from(groups, node_type=self.GROUP_NODE_TYPE)

    def remove_groups(self, groups):
        """ Remove nodes representing groups from graph by unique_ids

        Args:
            groups (list): list of string identifiers

        """
        self.__graph.remove_nodes_from(groups)

    def add_social_ties(self, social_ties):
        """ Connect agent nodes with directed edges in the graph.

        Args:
            social_ties

        """
        self.__graph.add_edges_from(social_ties, edge_type=self.SOCIAL_TIE_EDGE_TYPE)

    def remove_social_ties(self, social_ties):
        """ Remove directed edges between agent nodes.

        Args:
            social_ties

        """
        self.__graph.remove_edges_from(social_ties)

    def add_social_ties(self, social_ties):
        """ Connect agent nodes with directed edges in the graph.

        Args:
            social_ties

        """
        self.__graph.add_edges_from(social_ties, edge_type=self.SOCIAL_TIE_EDGE_TYPE)

    def remove_social_ties(self, identifications):
        """ Remove directed edges between group nodes.

        Args:
            identifications

        """
        self.__graph.remove_edges_from(identifications)

    """

    BEGIN GETTERS

    """

    def get_unique_id(self):
        return self.__unique_id

    def get_graph(self):
        return self.__graph

    def get_nodes(self, node_type=None):
        """ Get nodes of the graph with optional specificity by node type.

        Args:
            node_type (str): can be 'agent' or 'group'

        """
        __nodes = self.__graph.nodes.data()
        if node_type != None:
            return [node for node in __nodes if node[1]['node_type'] is node_type]
        else:
            return __nodes

    def get_number_of_nodes(self, node_type=None):
        """ Get number of nodes in the graph with optional specificity
            by node type.

        Args:
            node_type (str): can be 'agent' or 'group'

        """
        return len(self.get_nodes(node_type))

    def get_edges(self, edge_type=None):
        """ Get edges of the graph with optional specificity by edge type.

        Args:
            edge_type (str): can be 'social_tie' or 'identification'

        """
        __edges = self.__graph.edges.data()
        if edge_type != None:
            return [edge for edge in __edges if edge[1]['edge_type'] is edge_type]
        else:
            return __edges

    def get_number_of_edges(self, edge_type=None):
        """ Get number of edges in the graph with optional specificity
            by edge type.

        Args:
            edge_type (str): can be 'social_tie' or 'identification'

        """
        return len(self.get_edges(edge_type))
