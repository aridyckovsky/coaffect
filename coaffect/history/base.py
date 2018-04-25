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

    An example of a history object is given by `example_history` below,
    where each list element is indexed by a time step and each element
    is a dict of dicts (dict, where each measurable type, like 'participants',
    is associated with a dict representing the agent-state pairs saved at
    that time step).

    example_history = [

        {

            'participants': {
                'a0': {
                    'arousal': 0,
                    'position': (1, 0, 0),
                    'identifications': {
                        'g0': 0.73
                    }
                },
                ...
            },

            'groups': {
                'g0': {
                    'arousal': 0
                },
                'g1': {
                    'arousal': .24
                }
            },

            ''

        },
        ...

    ]

    """

    def __init__(self, experiment, record, steps=0):
        """ Initialize a History object for a given experiment.

        Args:
            experiment (obj): instance of experiment
            record (dict): dict of dict of states
            steps (int): number of steps, default to 0, empty history

        Attrs:
            _experiment (obj): experiment reference object
            _data (list): the history's data itself over steps + 1 entries

        """
        #: inherit trackable object attributes

        super().__init__()
        self._experiment = experiment
        #: TODO use schedule associated with experiment to determine length
        # of history data list
        self.__data = [record for s in range(0, steps)]

    def get_data(self):
        """ Get all recorded data from this history.

        """
        self._set_last_access()
        return self.__data

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
        self.__data[record.keys()[0]]
        self._set_last_modify()

    def bulk_modify(self, records, changes):
        for record in records:
            self.modify(record, changes[record])

    def insert(self, record):
        """ Insert a new record into the history's dataset.

        """
        self.__data.append(record)
        self._set_last_modify()
