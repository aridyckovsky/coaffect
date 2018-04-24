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
from ..history.base import History

class Experiment(object):
    """ Base class for Experiment framework.

    """

    #TODO: add 1-step iterator for experiment_ids that logs to records?
    def __init__(self, experiment_id, schedule, seed=None):
        """ Initialize an experiment with optional seed parameter.

        Args:
            experiment_id: integer identifier for experiment
            schedule: schedule instance
            seed: seed for random number generation

        Attrs:
            _experiment_id: unique id
            _running: boolean indicator to signal whether experiment is in progress
            _schedule: schedule object

        """

        self._experiment_id = experiment_id
        self._schedule = schedule

        self._running = False

        # Handle seed for random and numpy random number generation
        if seed is None:
            self.__seed = dt.datetime.now()
        else:
            self.__seed = seed
        random.seed(seed)
        numpy.random.seed(seed)

    def get_unique_id(self):
        return self._experiment_id

    def is_running(self):
        return self._running

    def run(self):
        """ Run experiment

        """
        self._running = True
        while self.is_running():
            self.step()

    def __iter__(self):
        return self

    def step(self):
        """ Step method required for all experiments. Override to use in
            practice. Note: subclasses will likely need a condition on
            `self.running`

        """
        self._schedule.next()
