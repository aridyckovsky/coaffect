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

    def __init__(self, unique_id, schedule, break_points=[], seed=None):
        """ Initialize an experiment with optional seed parameter.

        Args:
            experiment_id: integer identifier for experiment
            schedule: schedule instance
            break_points: optional time steps to pause the experiment
            seed: optional seed for random number generation

        Attrs:
            __unique_id: unique id
            __schedule: schedule object
            __running: boolean indicator to signal whether experiment is in progress
            __history: history object
            __break_points: time steps

        """
        super().__init__()
        self.__unique_id = unique_id
        self.__schedule = schedule
        self.__running = False
        self.__paused = False

        #: Create experiment's history with number of steps provided by
        #: schedule's length method
        self.__history = History(len(self.get_schedule()))

        #: Define break points as empty list
        self.__break_points = []

        # Handle seed for random and numpy random number generation
        if seed is None:
            self.__seed = dt.datetime.now()
        else:
            self.__seed = seed
        random.seed(seed)
        numpy.random.seed(seed)

    def run(self, break_points=[]):
        """ Run experiment for the duration of a schedule. If break points are
            defined, the experiment will run through a break point, at which
            the experiment will be paused until provided a command to continue.

        Args:
            break_points (list)

        """
        if break_points:
            self._set_break_points(break_points)
        if self.is_running() is True:
            print('Experiment is already running. Abort first in order to restart.')
        else:
            self.__running = True
            for time in self.__schedule:
                print('current time:', time)
                if time in self.__break_points:
                    self.pause()

    def pause(self):
        """ Pause the experiment.

        """
        self.__paused = True
        while self.is_paused():
            #: Upause by using the unpause method
            if self.is_paused() is False:
                break

    def unpause(self):
        """ Unpause the experiment.

        """
        self.__paused = False

    def restart(self):
        self.abort()
        self.run()

    def abort(self):
        """ Abort a current experiment run. History will be cleared by default.

        """
        self.__running = False
        self.__paused = False
        self.__schedule.reset()
        self.__history.reset()

    def _set_break_points(self, list_of_indices):
        """ Set the break points at which the experiment will be paused.

        """
        for index in list_of_indices:
            if index in self.get_history().get_indices() and index not in self.__break_points:
                self.__break_points.append(index)
            else:
                raise Exception("One or more of your break points is out of range.")

    def clear_break_points(self):
        self.__break_points = []

    def record(self, unique_id, measures):
        index = self.get_schedule().get_index()
        self.get_history().record(index, unique_id, measures)

    def __iter__(self):
        return self

    def __next__(self):
        """ Step method required for all experiments. Override to use in
            practice. Note: subclasses will likely need a condition on
            `self.running`

        """
        self.get_schedule().next()

    """

    BEGIN GETTERS

    """

    def get_unique_id(self):
        return self.__unique_id

    def get_schedule(self):
        return self.__schedule

    def get_history(self):
        return self.__history

    def is_running(self):
        return self.__running

    def is_paused(self):
        return self.__paused
