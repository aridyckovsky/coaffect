""" Create an Group of participants for experiment(s).

Core Object(s):
    Group

"""

#: Dependencies
import numpy
import random

class Group(object):
    """ Base class for Group object.

    """

    def __init__(self, _id, experiment):
        """ Initialize an agent with unique id.

        Args:
            _id: unique integer identifier
            experiment: reference to experiment group of participants is in

        """
        self._id = _id
        super().__init__(_id, experiment)

    def step(self):
        """ Step method required for all agents. Override to use in
            practice.

        """
        pass
