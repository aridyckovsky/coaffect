# group.py

""" group.py

Class: Group.

    Attributes:
        TODO

"""

import numpy as np
import scipy as sp
import networkx as nx
import random

class Group():

    def __init__(self, n_steps, n_agents, path_length, agent_positions, ties):

        self.graph = nx.DiGraph() # network structure
        self.n_agents = n_agents
        self.n_steps = n_steps
        self.path_length = path_length
        self.agent_positions = agent_positions

        self.agents = dict.fromkeys(np.arange(0, n_agents), {})
        self.ties = ties # list of edges for network structure

        self.current = {}
        self.current['expressing'] = {}
        self.current['stimulus'] = {}

        self.current['stimulus'] = {}
        self.current['stimulus'][0] = {
            'kind': 'harassment', #classification
            'position': 0,
            'duration': 1.0, # duration of stimulus effect
            'strength': 1.0, # scalar of force of stimulus
            'direction': 0.0 # direction of force of stimulus
        }

        self.history = {}
        self.history['stimulus'] = []

        self.data = {}
        self.data['group'] = np.zeros(n_steps + 1) # records of states of collective

    def populate(self, Agent):
        """Populate the group's agents, graph nodes and edges.

        Args:
            self (dict): Group object.
            Agent (dict): Agent class.

        """
        p = self.agent_positions
        for i in range(0, self.n_agents):

            a = Agent(i, self.n_steps, p[i])
            self.graph.add_node(i)
            self.agents[i] = a
            if i + 1 < self.n_agents:

                #: displacement of positions
                d = p[i + 1] - p[i]

                liking_a_b = 0
                liking_b_a = 0

                strength_a_b = np.random.random_sample()
                strength_b_a = np.random.random_sample()

                #: directed edge with weight from agent i to i + 1
                self.graph.add_edge(
                    i,
                    i + 1,
                    attr_dict={
                        'strength': strength_a_b,
                        'liking': liking_a_b,
                        'displacement': d
                    }
                )

                #: directed edge with weight from agent i + 1 to i
                self.graph.add_edge(
                    i + 1,
                    i,
                    attr_dict={
                        'strength': strength_b_a,
                        'liking': liking_b_a,
                        'displacement': d
                    }
                )

    def stimulations(self, step, dt):
        """Stimulate single agent noted by the current stimulus.

        Args:
            self (dict): Group object.
            step (int): time step
            dt (float): time increment

        """

        stimuli = self.current['stimulus']
        removals = []

        #: iterate through each stimulus in current situation
        for _id in stimuli:

            stimulus = stimuli[_id]
            effects = False

            #: apply stimulus to agents at stimulus position
            for a in self.agents:
                if (self.agents[a].position == stimulus['position']):

                    self.agents[a].stimulate(stimulus, _id, step, dt)
                    effects = True

            #: decrement duration of occurring stimulus by time increment
            if effects:
                stimulus['duration'] -= dt
            #: otherwise incremenet position by a positional step
            else:
                stimulus['position'] += 1

            #: add to history and remove stimulus if duration is 0 or less
            if stimulus['duration'] <= 0:
                removals.append(_id)

        #: add to history and remove stimulus if duration is 0 or less
        for _id in removals:
            self.history['stimulus'].append(self.current['stimulus'][_id])
            del self.current['stimulus'][_id]
        #: copy updated stimulus to current situation memory
        else:
            self.current['stimulus'][_id] = stimulus

    def reverberations(self):
        """Reverberated stimulations for small world situations.

        Args:
            self (dict): Group object.

        """
        pass

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

    def interactions(self, step, dt):
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

                #: perceiving agent
                b = self.agents[j]

                #: edge attrs for agents
                edge_a_b = self.graph[a._id][b._id]['attr_dict']
                edge_b_a = self.graph[b._id][a._id]['attr_dict']

                time = float(step) * dt

                #: express a --> b (read a expresses to b),
                #: percieve b --> a (read b perceives a)
                a.express(b, edge_a_b, time, dt)
                b.perceive(a, edge_b_a, time, dt)

    def update(self, step, dt):
        """Update agents and group.

        Args:
            self (dict): Group object.
            step (int): time step.
            dt (float): time interval.

        """
        # run interactions
        self.interactions(step, dt)

        #: run stimulations if any
        self.stimulations(step, dt)

        for i in self.agents:
            self.agents[i].update(step, dt)

        #: update expressing agents for interactions in next step
        self.expressing_agents()

        self.data['group'][step + 1] = len(self.current['expressing'])
