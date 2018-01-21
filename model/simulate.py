# simulate.py

""" simulate.py

Class: Simulate.

    Attributes:
        TODO

"""

import numpy as np

class Simulate():

    def __init__(self, T, dt):

        self.T = T
        self.dt = dt
        self.n_steps = int(round(self.T / self.dt))
        self.data = []

    # run: run simulator for groups of n_agents,
    #      with total time T and time interval dt
    def run(self, Group, Agent, n_agents, stimulations, ties, iterations):

        for i in range(iterations):

            group = Group(self.n_steps, n_agents, stimulations, ties)
            group.populate(Agent)

            for step in range(0, self.n_steps):
                group.update(step, self.dt)

            self.data.append({
                'agents': group.agents,
                'group': group.data
            })

    # output: return results of running simulator
    def output(self):
        return self.data
