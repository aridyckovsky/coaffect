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

    def __init__(self, steps):
        """ Initialize Time.

        Args:
            steps: integer number of steps

        """
        self._steps = steps
        #TODO: Implement iterator to use next() and run schedules

    def get_steps(self):
        return self._steps
