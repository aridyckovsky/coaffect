""" Create an Group of participants in environments.

Base Class:
    Group

Provided subclasses:
    EmotionalGroup

"""

#: Dependencies
import numpy
import random

from ..utils.tracking_object import TrackingObject
from ..utils.state import State

class Group(TrackingObject):
    """ Base class for Group object. Inherits TrackingObject's attributes.

    """

    MEMBER_IDS = 'member_ids'

    BASE_MEASURES = {
        MEMBER_IDS: []
    }

    def __init__(self, unique_id, experiment, measures={}, name=''):
        """ Initialize a uniquely identified group of members in an experiment,
            with the option to name it. Note that state is the 'collective state'
            of members, and members in a Group object are given as unique_ids of
            the actual members stored elsewhere.

        Args:
            unique_id (int): unique integer identifier
            experiment (obj): reference to experiment group is in
            measures (dict): group measures for state (like collective emotion)
            name (str): string identifier for convenient reference, if given

        Attrs:
            _experiment (obj)
            __unique_id (int)
            __name (str)
            __state (dict)

        """
        super().__init__()

        self.experiment = experiment
        self.__unique_id = unique_id
        self.__name = name

        measures.update(self.BASE_MEASURES)
        self.__state = State(measures)

    def set_name(self, new_name):
        """ Set a new name for the group.

        """
        self.__name = new_name

    def add_member_id(self, member_id):
        """ Add a new member's id to this group's state by appending to
            state measure of membership.

        Args:
            member_id (str)

        """
        if member_id not in self.get_measure(self.MEMBER_IDS):
            self.get_state().modify_measure(self.MEMBER_IDS, 'append', member_id)
        else:
            print('That member is already in the group!')
            #raise Exception('That member is already in the group!')

    def add_member_ids(self, list_of_member_ids):
        """ Add a list of new members by id to this group.

        Args:
            list_of_member_ids ([str])

        """
        for member_id in list_of_member_ids:
            self.add_member_id(member_id)

    def update(self):
        """ Update method required for all groups. Subclasses may (and should)
            specialize and extend as necessary. Records current measures to
            experiment's history.

        """
        self.experiment.record(self.get_unique_id(), self.get_measures())

    """

    BEGIN GETTERS

    """

    def get_unique_id(self):
        """ Return unique_id.

        """
        return self.__unique_id

    def get_name(self):
        """ Return name, if given, else pass.

        """
        return self.__name if self.__name else 'No Name'

    def get_experiment_id(self):
        """ Retur experiment id group is a part of for reference.

        """
        return self.experiment.get_unique_id()

    def get_state(self):
        """ Return state of group.

        """
        return self.__state

    def get_measures(self):
        """ Return measures in state.

        """
        return self.get_state().get_measures()

    def get_measure(self, measure_name):
        """ Return measure by name in state.

        """
        return self.get_state().get_measure(measure_name)

    def get_member_ids(self):
        """ Return member_ids measure.

        """
        return self.get_measure(self.MEMBER_IDS)
