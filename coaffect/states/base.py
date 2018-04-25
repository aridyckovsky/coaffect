""" State is a general use data container for an active object's current
    state of measureable features.

Base Class:
    State

"""

import numpy

class State(object):
    """ Base class for State.

    """
    def __init__(self, measures):
        """ Initialize State, converting measures to State requirements.

        Args:
            measures (dict): A string-only dictionary mapping labels to types

        Attrs:
            _measures (dict)

        """
        self._measures = {l: d for (l,d) in measures.items()}

    def get_measures(self):
        """ Get all measures from the state in standard format.

        """
        return self._measures

    def get_measure_by_label(self, label):
        """ Get a singular measure by its label.

        Args:
            label (str)

        """
        try:
            return self._measures[label]
        except KeyError:
            raise

    def _set_measure_by_label(self, label, new_val):
        """ Set a singular measure by its label.

        Args:
            label (str)
            new_val (type relative to old_val)
        """
        try:
            self._measures[label] = new_val
        except KeyError:
            raise
        except ValueError:
            raise
