""" Create, run, import and export data with Experiment class for
    various agent-based network models.

Base Class:
    Experiment

Subclasses:
    Simulation (virtual experiment)

"""

#: Dependencies
import datetime as dt
import numpy
import random

from ..utils.tracking_object import TrackingObject
from ..environments.base import Environment
from ..history.base import History

class Experiment(TrackingObject):
    """ Base class for Experiment framework.

    """

    def __init__(self, unique_id, schedule, seed=None):
        """ Initialize an experiment with optional seed parameter.

        Args:
            unique_id: str identifier for experiment
            schedule: schedule instance
            seed: optional seed for random number generation

        Attrs:
            __unique_id: unique id
            __schedule: schedule object
            __running: boolean indicator to signal whether experiment is in progress
            __history: history object

        """
        super().__init__()
        self._unique_id = unique_id
        self._schedule = schedule
        self._index = self._schedule.get_index()
        self._running = False

        #: Create experiment's history with number of steps provided by
        #: schedule's length method
        self._history = History(len(self.get_schedule()))

        # Handle seed for random and numpy random number generation
        if seed is None:
            self._seed = dt.datetime.now()
        else:
            self._seed = seed
        random.seed(seed)
        numpy.random.seed(seed)

    def __repr__(self):
        return 'Experiment({})'.format(self._unique_id)

    def run(self):
        """ Run experiment. Must extend in subclasses for usage.

        """
        if self.is_running() is True:
            print('Experiment is already running. \
                  Abort first in order to restart.')
        self._running = True
        while self.is_running():
            # if data, record, otherwise, do nothing
            pass

    def stop(self):
        """ Stop experiment.

        """
        self._running = False

    def restart(self):
        self.stop()
        self.reset()
        self.run()

    def reset(self):
        """ Reset a current experiment run. History will be cleared by default.

        """
        self._running = False
        self._schedule.reset()
        self._history.reset()

    def record(self, unique_id, measures):
        index = self._schedule.get_index()
        self._history.record(index, unique_id, measures)

    """

    BEGIN GETTERS

    """

    def get_unique_id(self):
        return self._unique_id

    def get_schedule(self):
        return self._schedule

    def get_history(self):
        return self._history

    def is_running(self):
        return self._running
