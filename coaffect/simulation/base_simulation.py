""" Create, run, import and export data with the Simulation class for
    various agent-based network models.

Base Class:
    Simulation

"""

#: Dependencies
import datetime as dt
import numpy
import random

from ..utils.trackable_object import TrackableObject
from ..environment.base_environment import Environment
from ..history.base_history import History

class Simulation(TrackableObject):
    """ Base class for Simulation.

    """

    def __init__(self, unique_id, schedule, seed=None):
        """ Initialize simulation, a virtual experiment, with optional pre-set
            pause times (break_points).

        Args:
            unique_id: str identifier for experiment
            schedule: schedule instance
            break_points: optional time steps to pause the experiment
            seed: optional seed for random number generation

        Attrs:
            _unique_id: unique id
            _schedule: schedule object
            _running: boolean indicator to signal whether simulation
                        is in progress
            _paused: boolean indicator to signal whether simulation
                        is paused
            _history: history object
            _break_points: time steps

        """
        super().__init__()
        self._unique_id = unique_id
        self._schedule = schedule
        self._index = self._schedule.get_index()
        self._running = False

        #: Create experiment's history with number of steps provided by
        #: schedule's length method
        self._history = History(len(self.get_schedule()))

        #: Define break points as empty list
        self._break_points = []

        #: Allow for pauses, set default to false
        self._paused = False

        # Handle seed for random and numpy random number generation
        if seed is None:
            self._seed = dt.datetime.now()
        else:
            self._seed = seed
        random.seed(seed)
        numpy.random.seed(seed)

    def __repr__(self):
        return 'Simulation({})'.format(self._unique_id)

    def __eq__(self, other):
        #TODO must be same class!!!
        return self.get_unique_id() == other.get_unique_id()

    def _set_break_points(self, list_of_indices):
        """ Set the break points at which the experiment will be paused.

        """
        for index in list_of_indices:
            if index in self._break_points:
                pass
            elif (index in self.get_history().get_indices() and
                    index not in self._break_points):
                self._break_points.append(index)
            else:
                raise Exception("One or more of your break \
                                points is out of range.")

    def clear_break_points(self):
        self._break_points = []

    def run(self, break_points=[]):
        """ Run simulation for the duration of a schedule. If break points are
            defined, the experiment will run through a break point, at which
            the experiment will be paused until provided a command to continue.

        Args:
            break_points (list)

        """

        if break_points:
            self._set_break_points(break_points)

        if self.is_running() is True:
            print('Simulation is already running. Stop first in \
                  order to restart.')
        else:
            self._running = True
            for point in self._schedule:
                index = self._schedule.get_index()

                # TODO: provide update method for all objects with state
                #self._environment.update()
                # TODO: record all updates to history

                # pause after step completes if requested
                if index in self._break_points:
                    self.pause()
                    while self.is_paused():
                        phrase = input('Enter the word "unpause" to continue: ')
                        if phrase == 'unpause':
                            self.unpause()
                            break

    def stop(self):
        """ Stop experiment.

        """
        self._running = False
        self.unpause()

    def pause(self):
        """ Pause the experiment.

        """
        self._paused = True
        print('Simulation paused at schedule index',
                self.get_schedule().get_index())

    def unpause(self):
        """ Unpause the experiment.

        """
        self._paused = False

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
        self.unpause()

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

    def get_break_points(self):
        return self._break_points

    def is_running(self):
        return self._running

    def is_paused(self):
        return self._paused
