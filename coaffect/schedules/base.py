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
            __start (int)
            __curr (int): current time in seconds
            __duration (int): total number of seconds
            __resolution (int): number of seconds to jump in iter

        """
        self.__start = 0
        self.__curr = 0

        dur = 0
        if 'days' in duration:
            dur += duration['days'] * self.DAYS_TO_SECONDS
        if 'hours' in duration:
            dur += duration['hours'] * self.HOURS_TO_SECONDS
        if 'minutes' in duration:
            dur += duration['minutes'] * self.MINUTES_TO_SECONDS
        if 'seconds' in duration:
            dur += duration['seconds']

        if dur is 0:
            raise Exception('Cannot have a schedule with zero duration.')

        self.__duration = dur
        self.__resolution = resolution
        self.__index = round(self.__curr / self.__resolution)

    def __repr__(self):
        return 'Schedule({}, {})'.format(self.__duration, self.__resolution)

    def __len__(self):
        """ Custom length method to return number of time steps defined by
            a schedule.

        """
        return round(self.get_duration() / self.get_resolution()) + 1

    def __iter__(self):
        """ Make Schedule object iterable.

        """
        return self

    def __next__(self):
        """ Define process of iteration, stop at end as final time.

        Args:
            resolution (int): If defined, the number of time seconds to jump

        """
        if self.__curr < self.__duration:
            new = self.__curr
            self.__curr += self.__resolution
            self.__index = round(new / self.__resolution)
            return new
        else:
            raise StopIteration()

    def reset(self):
        """ Reset the time back to start.

        """
        new = self.__start
        self.__curr = new

    def _set_resolution(self, res):
        """ Set resolution in seconds.

        Args:
            res (int): desired new resolution

        """
        self.__resolution = res

    """

    BEGIN GETTERS

    """

    def get_curr(self):
        return self.__curr

    def get_index(self):
        return self.__index

    def get_duration(self):
        return self.__duration

    def get_resolution(self):
        return self.__resolution
