""" Create, collect, edit, and delete records of "historical" data for and from experiments.
    We consider a record a full, time-indexed dataset for a given experiment, whether
    virtual or not.

Base Class:
    History (extends collections.defaultdict)

"""

#: Dependencies
import numpy
import random
import pandas

from ..utils.tracking_object import TrackingObject

class History(TrackingObject):
    """ Base class for History. Extends TrackingObject by default.

    """

    def __init__(self, indices):
        """ Initialize a History object for a given experiment.

        Args:
            indices (int): number of indices for list of data

        Attrs:
            __data (list): the history's data itself over steps + 1 entries

        """
        #: inherit trackable object attributes

        super().__init__()

        self.__data = [{} for i in range(indices)]

    def record(self, index, unique_id, measures):
        """ Record a given object's measures, mapped to a unique id, at a given
            index.

        """
        self.__data[index][unique_id] = measures
        self._set_last_modify()

    """

    BEGIN GETTERS

    """

    def get_data(self):
        """ Get all recorded data from this history.

        """
        self._set_last_access()
        return self.__data

    def get_record(self, index):
        """ Get record by index.

        """
        self._set_last_access()
        return self.__data[index]
