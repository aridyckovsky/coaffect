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

from ..utils.trackable_object import TrackableObject

class History(TrackableObject):
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

        self.__indices = range(indices)
        self.__data = [{} for i in self.__indices]

    def __repr__(self):
        """ Output representation of History object with number of indices (len).

        """
        return 'History({})'.format(len(self.__indices))

    def __len__(self):
        return len(self.__indices)

    def record(self, index, unique_id, measures):
        """ Record a given object's measures, mapped to a unique id, at a given
            index.

        """
        self.__data[index][unique_id] = measures
        self._set_last_modify()

    def reset(self):
        """ Reset the history's data to original list of empty dicts.

        """
        self.__data = [{} for i in self.__indices]

    """

    BEGIN GETTERS

    """

    def get_data(self):
        """ Get all recorded data from this history.

        """
        self._set_last_access()
        return self.__data

    def get_indices(self):
        """ Get iterable indices.

        """
        self._set_last_access()
        return self.__indices

    def get_record(self, index):
        """ Get record by index.

        """
        self._set_last_access()
        return self.__data[index]
