""" TrackingObject is a utility class as a base class for data structures or classes
    that require certain tracking references such as time of creation, last
    modification, etc.

"""

from datetime import datetime

class TrackingObject(object):

    def __init__(self):

        current_time = datetime.now()
        self.__created_at = current_time
        self.__last_modified_at = current_time
        self.__last_accessed_at = current_time

    def _set_last_modify(self):
        """ Set the time of last modification to the trackable object.

        """
        self.__last_modified_at = datetime.now()

    def _set_last_access(self):
        """ Set the time of last access to the trackable object.

        """
        self.__last_accessed_at = datetime.now()
