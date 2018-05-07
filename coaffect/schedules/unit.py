""" UnitSchedule is a subclass extension and override of Schedule
    that provides a convenient choice system for resolutions of
    unit type, such as 1 second, 1 minute, 1 hour, etc.

"""

from .base import Schedule

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

        if unit == 'second':
            self._set_resolution(self.SECOND)
        elif unit == 'minute':
            self._set_resolution(self.MINUTES_TO_SECONDS)
        elif unit == 'hour':
            self._set_resolution(self.HOURS_TO_SECONDS)
        elif unit == 'day':
            self._set_resolution(self.DAYS_TO_SECONDS)
        else:
            self._set_resolution(self.SECOND)
