""" Say something about record class.

Core Object(s):
    Record

"""

#: Dependencies
import numpy
import random
import pandas
import collections

class Network(object):
    """ Base class for Network.

    """

    def __init__(self, experiment, _id):
        """ Initialize a NetworkX network of participant objects.

        Args:
            model: instance of model

        Attrs:
            _id: a unique identifier for the network

        """
        super().__init__(experiment)
        self._id = _id
