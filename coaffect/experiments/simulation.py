""" Simulate a virtual experiment.

"""

import datetime
import numpy
import random

from .base import Experiment

class Simulation(Experiment):

    def __init__(self, experiment_id, schedule, seed=None):
        """ Initialize simulation, a virtual experiment.

        """
        super().__init__(experiment_id, schedule, seed)
