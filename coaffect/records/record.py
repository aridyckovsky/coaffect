""" Create, collect, edit, and delete records of data for and from experiments.

Core Object(s):
    Record

"""

#: Dependencies
import numpy
import random
import pandas
import collections

class Record(object):
    """ Base class for Record.

    """

    def __init__(self, experiment, _id):
        """ Initialize a Record object for a given experiment.

        Args:
            model: instance of model

        Attrs:
            _id: a unique identifier for the network

        """
        super().__init__(experiment)
        self._id = _id
