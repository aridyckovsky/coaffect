""" TrackingObject is a utility class as a base class for data structures or classes
    that require certain tracking references such as time of creation, last
    modification, etc.

Public methods for all registered subclasses:
    tracking_info: provides metadata collected by TrackingObject

"""

from datetime import datetime

class TrackingObject():
    """ TrackingObject is a trackable object for metadata.

    """

    def __init__(self):
        current_time = datetime.now()
        self.__created_at = current_time
        self.__last_modified_at = current_time
        self.__last_accessed_at = current_time

    def __repr__(self):
        return "TrackingObject()"

    def _set_last_modify(self):
        """ Set the time of last modification to the trackable object.

        """
        self.__last_modified_at = datetime.now()

    def _set_last_access(self):
        """ Set the time of last access to the trackable object.

        """
        self.__last_accessed_at = datetime.now()

    def tracking_info(self):
        """ Get tracking information (the private attributes to this object)
            that acts as metadata for a given instance of a TrackingObject
            subclass.

        Returns a dictionary mapping of tracked meta-measures.

        """
        return dict(
            created_at=self.__created_at,
            last_modified_at=self.__last_modified_at,
            last_accessed_at=self.__last_accessed_at
        )
