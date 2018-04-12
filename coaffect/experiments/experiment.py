""" Create, run, import and export data with Experiment class for
    various agent-based network models.

Core Object(s):
    Experiment

Note: Inspiration taken from Project Mesa's base model object.

"""

#: Dependencies
import datetime
import numpy
import random

from .environment import Environment

class Experiment(object):
    """ Base class for Experiment framework.

    """

    def __init__(self, _id, seed=None):
        """ Initialize an experiment with optional seed parameter.

        Args:
            _id: unique integer identifier
            seed: seed for random number generation

        Attrs:
            running: boolean indicator to signal whether experiment is in progress
            schedule: schedule object

        """
        super().__init__(_id)
        self.running = True
        self.schedule = None

        # Handle seed for random and numpy random number generation
        if seed is None:
            self.seed = dt.datetime.now()
        else:
            self.seed = seed
        random.seed(seed)
        numpy.random.seed(seed)

    def run(self):
        """ Run experiment

        """
        while self.running:
            self.step()

    def step(self):
        """ Step method required for all experiments. Override to use in
            practice. Note: subclasses will likely need a condition on
            `self.running`

        """
        pass
