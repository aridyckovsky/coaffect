# group.py

""" group.py

Class: Group.

    Attributes:
        TODO

"""

import numpy as np
import scipy as sp
import networkx as nx

class Group():

    def __init__(self, n_steps, n_agents, stimulations, ties):

        self.graph = nx.DiGraph() # network structure
        self.n_agents = n_agents
        self.n_steps = n_steps

        self.agents = dict.fromkeys(np.arange(1, n_agents + 1), {})
        self.stimulations = stimulations
        self.ties = ties # list of edges for network structure

        self.current = {}
        self.current['expressing'] = {}
        self.data = {}
        self.data['group'] = np.zeros(n_steps + 1) # records of states of collective

    def populate(self, Agent):
        """Populate the group's agents, graph nodes and edges.

        Args:
            self (dict): Group object.
            Agent (dict): Agent class.

        """

        for i in range(1, self.n_agents + 1):

            a = Agent(i, self.n_steps)
            self.graph.add_node(i)
            self.agents[i] = a

        self.graph.add_weighted_edges_from(self.ties)

    def stimulate(self, stimulus):
        """Stimulate agents noted by the current stimulus.

        Args:
            self (dict): Group object.
            stimulus (dict): Stimulus object.

        """

        for a in stimulus['agents']:
            self.agents[a].stimulate(stimulus)

    def expressing_agents(self):
        """Get list of expressing agents from group self.

        Args:
            self (dict): Group object.

        """

        e = {}

        for a in self.agents:
            if self.agents[a].above_act_thr():
                e[a] = self.agents[a]

        self.current['expressing'] = e

    def interactions(self):
        """Run interactions for expressing agents; also for perceiving
            agents if above recharge boundary.

        Args:
            self (dict): Group object.

        """
        # TODO: an agent should be able to interact with a subgroup,
        #   not just single agents, even if simultaneously.
        # TODO: interactions should not happen every step, but probabilistically
        #   relative to tie strength. The tie weight should not influence the
        #   interaction, from expression and perception perspectives, as it is
        #   more appropriately a factor of tie strength?

        #: get currently expressing agents
        e = self.current['expressing']

        #: iterate through expressing agents
        for i in e:

            a = e[i]

            #: get neighbors of currently expressing agent
            neighbors = nx.all_neighbors(self.graph, a._id)

            #: iterate through neighbors
            for j in neighbors:

                b = self.agents[j]

                weight_a_b = self.graph[a._id][b._id]['weight']
                self.graph[a._id][b._id]['weight'] = a.express(b, weight_a_b)

                weight_b_a = self.graph[b._id][a._id]['weight']
                self.graph[b._id][a._id]['weight'] = b.perceive(a, weight_b_a)

                #if b.above_rec_thr():
                    #weight_b_a = self.graph[b._id][a._id]['weight']
                    #self.graph[b._id][a._id]['weight'] = b.perceive(a, weight_b_a)

    def update(self, step, dt):
        """Update agents and group.

        Args:
            self (dict): Group object.
            step (int): time step.
            dt (float): time interval.

        """

        if step in self.stimulations:
            self.stimulate(self.stimulations[step])

        self.interactions()

        for i in self.agents:
            self.agents[i].update(step, dt)

        self.expressing_agents()

        self.data['group'][step + 1] = len(self.current['expressing'])
