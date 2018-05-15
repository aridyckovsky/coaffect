""" Simulate a virtual experiment.

"""

import datetime
import numpy
import random

from .base import Experiment

class Simulation(Experiment):

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
        super().__init__(unique_id, schedule, seed)

        #: Define break points as empty list
        self._break_points = []

        #: Allow for pauses, set default to false
        self._paused = False

    def __repr__(self):
        return 'Simulation({})'.format(self._unique_id)

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
                #self.__environment.update()
                # TODO: record all updates to history

                # pause after step completes if requested
                if index in self._break_points:
                    self.pause()
                    while self.is_paused():
                        phrase = input('Enter the word "unpause" to continue: ')
                        if phrase == 'unpause':
                            self.unpause()
                            break

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

    def stop(self):
        """ Extend Experiment stop method to end any pauses.

        """
        super().stop()
        self.unpause()

    def reset(self):
        """ Extend Experiment reset method to end any pauses.

        """
        super().reset()
        self.unpause()

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

    """

    BEGIN GETTERS

    """

    def get_break_points(self):
        return self._break_points

    def is_paused(self):
        return self._paused
