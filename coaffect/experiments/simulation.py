""" Simulate a virtual experiment.

"""

import datetime
import numpy
import random

from .base import Experiment

class Simulation(Experiment):

    def __init__(self, experiment_id, seed=None):
        super().__init__(experiment_id, seed)
        
