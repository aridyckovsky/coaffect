""" Create an Group of participants in environments.

Base Class:
    Group

Subclasses:

"""

#: Dependencies
import numpy
import random

class Group(object):
    """ Base class for Group object.

    """

    def __init__(self, unique_id, experiment, members=[], name=''):
        """ Initialize a uniquely identified group of members in an experiment,
            with the option to name it. Note that state is the 'collective state'
            of members, and members in a Group object are given as unique_ids of
            the actual members stored elsewhere.

        Args:
            unique_id (int): unique integer identifier
            experiment (obj): reference to experiment group is in
            members (list): unique_ids of agents to include in group, if any
            name (str): string identifier for convenient reference, if given

        Attrs:
            _unique_id (int)
            _experiment (obj)
            _members (list)
            _name (str)
            _state (dict)

        """
        self._unique_id = unique_id
        self._experiment = experiment
        self._members = members
        self._name = name

        self._state = {}

    def get_unique_id(self):
        """ Return unique_id.

        """
        return self._unique_id

    def get_experiment(self):
        """ Return experiment.

        """
        return self._experiment

    def get_members(self):
        """ Return current members.

        """
        return self._members

    def get_state(self):
        """ Return state of collective.

        """
        return self._state

    def get_name(self):
        """ Return name, if given, else pass.

        """
        return self._name if self._name else pass

    def _set_members(self, members_to_remove, new_members):
        """ Set list of members. First remove old members, then add new members.

        """
        for r in members_to_remove:
            self._members.remove(r)
        self._members = self._members + new_members


    def _set_state(self):
        """ Set a new state.

        """
        pass

    def _set_name(self, new_name):
        """ Set a new name for the group.

        """
        self._name = new_name

    def step(self):
        """ Step method required for all groups. Override to use in
            practice.

        Requirements: Define in subclasses.

        """
        pass
