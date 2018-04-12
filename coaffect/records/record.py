""" Create, collect, edit, and delete records of data for and from experiments.

Base Class:
    Record (extends collections.defaultdict)

"""

#: Dependencies
import numpy
import random
import pandas
from collections import defaultdict

class Record(defaultdict):
    """ Base class for Record.

    """

    def __init__(self, experiment):
        """ Initialize a Record object for a given experiment.

        Args:
            experiment: instance of experiment

        Attrs:
            _experiment (obj)

        """
        self._experiment = experiment
        self._data = []

    def get_data(self):
        return self._data
