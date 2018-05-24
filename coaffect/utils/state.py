""" State is a general use data container for an active object's current
    state of measureable features.

Base Class:
    State

"""

import numpy

from .trackable_object import TrackableObject

class State(TrackableObject):
    """ Base class for State. State tracks and remembers a dict of measures,
        which are modifiable attributes of classes that have State.

    """

    #: Default modification types
    ADD = 'add'
    SUBTRACT = 'subtract'
    MULT = 'multiply'
    DIVIDE = 'divide'
    APPEND = 'append'
    REMOVE = 'remove'
    RESET = 'reset'

    def __init__(self, measures):
        """ Initialize State, converting measures to State requirements.

        Args:
            measures (dict): A string-only dictionary mapping labels to types

        Attrs:
            __measures (dict)

        """
        super().__init__()
        self.__measures = {name: val for (name,val) in measures.items()}

    def __repr__(self):
        return 'State({})'.format(self.__measures)

    def _set_measure(self, name, new_val):
        """ Set a measure to a new value.

        """
        self.__measures[name] = new_val
        self._set_last_modify()

    def modify_measure(self, name, mod_type, mod_val):
        """ Modify a measure with a specific modification type (operation) on
            the current value and the modification value provided.

        """
        curr_val = self.get_measure(name)

        #: Arithmetic operations for appropriate types
        if mod_type == self.ADD:
            new_val = curr_val + mod_val
        if mod_type == self.SUBTRACT:
            new_val = curr_val - mod_val
        if mod_type == self.MULT:
            new_val = curr_val * mod_val
        if mod_type == self.DIVIDE:
            if mod_val is not 0:
                new_val = curr_val / mod_val

        #: List-like operations for appropriate types
        if mod_type == self.APPEND:
            curr_val.append(mod_val)
            new_val = curr_val
        if mod_type == self.REMOVE:
            if mod_val in curr_val:
                curr_val.remove(mod_val)
                new_val = curr_val
            else:
                pass

        #: Reset operation
        if mod_type == self.RESET:
            new_val = mod_val

        #: Set the named measure to the new value
        self._set_measure(name, new_val)

    """

    BEGIN GETTERS

    """

    def get_measures(self):
        """ Get all measures in state.

        """
        self._set_last_access()
        return self.__measures

    def get_measure(self, name):
        """ Get measure by name.

        """
        return self.get_measures()[name]
