""" Schedule is a base class for building temporal schedules and providing
    timelines in various formats for analysis.

Base Class:
    Schedule

Subclasses:
    UnitSchedule

"""

#: Dependencies
import datetime
import numpy
import random

from ..utils.tracking_object import TrackingObject

class Schedule(TrackingObject):
    """ Base class for Schedule.

    """

    SECOND = 1
    MINUTES_TO_SECONDS = 60 * SECOND
    HOURS_TO_SECONDS = 60 * MINUTES_TO_SECONDS
    DAYS_TO_SECONDS = 24 * HOURS_TO_SECONDS

    def __init__(self, duration, resolution=1):
        """ Initialize instance of Schedule.

        Args:
            start (int): beginning step
            duration (dict): total time, given as dict
            resolution (int): number of seconds

        Example of duration dict:

        example_duration = {
            'days': 2,
            'hours': 3,
            'minutes': 30,
            'seconds': 30
        }

        Attrs:
            _start (int)
            _state (int): current time in seconds
            _duration (int): total number of seconds
            _resolution (int): number of seconds to jump in iter

        """
        self._start = 0
        self._state = 0

        self._duration = 0
        self._duration += duration['days'] * self.DAYS_TO_SECONDS
        self._duration += duration['hours'] * self.HOURS_TO_SECONDS
        self._duration += duration['minutes'] * self.MINUTES_TO_SECONDS
        self._duration += duration['seconds']

        self._resolution = resolution

    def __iter__(self):
        """ Make Schedule object iterable.

        """
        return self

    def next(self):
        """ Define process of iteration, stop at end as final time.

        Args:
            resolution (int): If defined, the number of time seconds to jump

        """
        if self._state < self._duration:
            _state = self._state
            self._state += self._resolution
            return _state
        else:
            raise StopIteration()

    def reset(self):
        """ Reset the time back to start.

        """
        _start = self._start
        self._state = _start

    #: Set Attributes
    def _set_resolution(self, res):
        """ Set resolution in seconds.

        Args:
            res (int): desired new resolution

        """
        self._resolution = res

    #: Get Attributes
    def get_state(self):
        return self._state

    def get_duration(self):
        return self._duration

    def get_resolution(self):
        return self._resolution

    def get_duration(self):
        return self._duration
