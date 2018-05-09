""" Create, run, import and export data with Experiment class for
    various agent-based network models.

Base Class:
    Experiment

Subclasses:
    Simulation (virtual experiment)

Note: Inspiration taken from Project Mesa's base model object.

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

    #TODO: add 1-step iterator for experiment_ids that logs to records?
    def __init__(self, unique_id, schedule, seed=None):
        """ Initialize an experiment with optional seed parameter.

        Args:
            experiment_id: integer identifier for experiment
            schedule: schedule instance
            seed: seed for random number generation

        Attrs:
            __unique_id: unique id
            __schedule: schedule object
            __running: boolean indicator to signal whether experiment is in progress
            __history: history object

        """
        super().__init__()
        self.__unique_id = unique_id
        self.__schedule = schedule
        self.__running = False

        # Handle seed for random and numpy random number generation
        if seed is None:
            self.__seed = dt.datetime.now()
        else:
            self.__seed = seed
        random.seed(seed)
        numpy.random.seed(seed)

        #: Create experiment's history with number of steps provided by
        #: schedule's length method
        self.__history = History(len(self.get_schedule()))

    def run(self):
        """ Run experiment

        """
        self.__running = True
        while self.is_running():
            self.next()

    def record(self, unique_id, measures):
        index = self.get_schedule().get_index()
        self.get_history().record(index, unique_id, measures)

    def __iter__(self):
        return self

    def next(self):
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
        return self.__is_running
