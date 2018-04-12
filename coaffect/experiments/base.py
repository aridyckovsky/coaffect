""" Create, run, import and export data with Experiment class for
    various agent-based network models.

Base Class:
    Experiment

Subclasses:
    Simulation (virtual experiment)

Note: Inspiration taken from Project Mesa's base model object.

"""

#: Dependencies
import datetime
import numpy
import random

from ..environments.base import Environment
from ..records.base import Record

class Experiment(object):
    """ Base class for Experiment framework.

    """

    #TODO: add 1-step iterator for experiment_ids that logs to records?
    def __init__(self, experiment_id, seed=None):
        """ Initialize an experiment with optional seed parameter.

        Args:
            experiment_id: integer identifier for experiment
            seed: seed for random number generation

        Attrs:
            running: boolean indicator to signal whether experiment is in progress
            schedule: schedule object

        """
        self._experiment_id = experiment_id
        self._running = True
        self._schedule = None

        # Handle seed for random and numpy random number generation
        if seed is None:
            self.__seed = dt.datetime.now()
        else:
            self.__seed = seed
        random.seed(seed)
        numpy.random.seed(seed)

    def get_id(self):
        return self._experiment_id

    def is_running(self):
        return self._running

    def run(self):
        """ Run experiment

        """
        while self.is_running():
            self.step()

    def step(self):
        """ Step method required for all experiments. Override to use in
            practice. Note: subclasses will likely need a condition on
            `self.running`

        """
        pass
