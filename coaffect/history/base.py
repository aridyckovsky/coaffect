""" Create, collect, edit, and delete records of "historical" data for and from experiments.
    We consider a record a full, time-indexed dataset for a given experiment, whether
    virtual or not.

Base Class:
    History (extends collections.defaultdict)

"""

#: Dependencies
import datetime
import numpy
import random
import pandas
from collections import defaultdict

class History(defaultdict):
    """ Base class for Record.

    """

    def __init__(self, experiment, states):
        """ Initialize a History object for a given experiment.

        Args:
            experiment (obj): instance of experiment
            states (dict): dict of dicts

        Attrs:
            _experiment (obj): experiment reference object
            _data (obj): the history's data itself
            __created_at (datestr): timestamp for record creation
            __last_accessed_at (datestr): timestemp for last access
            __last_modified_at (datestr): timestemp for last edit

        """
        self._experiment = experiment
        self._data = []

        #: Private attributes
        self.__created_at = datetime.now()
        self.__last_accessed_at = datetime.now()
        self.__last_modified_at = datetime.now()

    def __set_last_access(self):
        self.__last_accessed_at = datetime.now()

    def __set_last_modify(self):
        self.__last_modified_at = datetime.now()

    def get_data(self):
        """ Get all recorded data from this history.

        """
        self.__set_last_access()
        return self._data

    def get_record(self, index):
        """ Get the current record in full, or with options.

        """
        return self.get_data()[index]

    def get_record_list(self, indices):
        """
        """
        pass

    def get_labels(self):
        pass

    def modify(self, record, change):
        self._data[record.keys()[0]]

    def bulk_modify(self, records, changes):
        for record in records:
            self.modify(record, changes[record])

    def insert(self, record):
        """ Insert a new record into the history's dataset.

        """
        self.__set_last_modify()
        self.__data.append(record)
