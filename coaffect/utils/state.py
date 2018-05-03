""" State is a general use data container for an active object's current
    state of measureable features.

Base Class:
    State

"""

import numpy

from .tracking_object import TrackingObject

class State(TrackingObject):
    """ Base class for State. Inherits TrackingObject's attributes.

    """
    def __init__(self, measures):
        """ Initialize State, converting measures to State requirements.

        Args:
            measures (dict): A string-only dictionary mapping labels to types

        Attrs:
            _measures (dict)

        """
        super().__init__()
        self._measures = {l: d for (l,d) in measures.items()}

    def _set_measure(self, feature, value):
        """ Convenient setter for updating a single measure of a state.

        Args:
            feature (str)
            value (instanceof feature)

        """
        if instanceof(value) is instanceof(self._measures[feature]):
            self._measures[feature] = value
            self._set_last_modify()
        else:
            raise ValueException('This is the wrong data type!')

    def _set_state(self, measures):
        """ Convenient setter for updating a state with multiple measures at once.

        Args:
            measures (dict)

        """
        for m in measures:
            self._set_measure(m, measures[m])

    def get_measures(self):
        """ Get all measures from the state in standard format.

        """
        self._set_last_access()
        return self._measures