""" UnitSchedule is a subclass extension and override of Schedule
    that provides a convenient choice system for resolutions of
    unit type, such as 1 second, 1 minute, 1 hour, etc.

"""

from .base_schedule import Schedule

class UnitSchedule(Schedule):
    """ UnitSchedule is a subclass of Schedule to associate with
        experiments.

    """
    def __init__(self, duration, unit='second'):
        """ Initialize a unit schedule instance.

        Args:
            duration
            unit

        """
        super().__init__(duration)
        self.__unit = unit

        if self.__unit == 'second':
            self._set_resolution(self.SECOND)
        elif self.__unit == 'minute':
            self._set_resolution(self.MINUTES_TO_SECONDS)
        elif self.__unit == 'hour':
            self._set_resolution(self.HOURS_TO_SECONDS)
        elif self.__unit == 'day':
            self._set_resolution(self.DAYS_TO_SECONDS)
        else:
            self._set_resolution(self.SECOND)

    def __repr__(self):
        return 'UnitSchedule({}, {})'.format(self.get_duration(),
                                             self.get_unit())

    """

    BEGIN GETTERS

    """

    def get_unit(self):
        return self.__unit
