""" Say something about time class.

Base Class:
    Time

"""

#: Dependencies
import datetime
import numpy
import random

class Time(object):
    """ Base class for Time.

    """

    #TODO: make relative to real time measures (seconds, days, etc.)
    def __init__(self, start, duration, interval=1.0):
        """ Initialize Time.

        Args:
            start (int): beginning step
            duration (float): total time
            interval (float): time interval of interest

        """
        self._state = start
        self._duration = duration
        self._interval = interval
        self._end = round(duration / interval) + 1

    def __iter__(self):
        """ Make Time object iterable.

        """
        return self

    def next(self, step=1):
        """ Define process of iteration, stop at end as final time.

        Args:
            step (int): If defined, the number of time steps skipped

        """
        if self._state < self._end:
            _state = self._state
            self._state += step
            return _state
        else:
            raise StopIteration()

    def get_state(self):
        return self._state

    def get_duration(self):
        return self._duration

    def get_interval(self):
        return self._interval

    def get_end(self):
        return self._end
