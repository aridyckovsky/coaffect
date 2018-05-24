# -*- coding: utf-8 -*-
""" Coaffect Schedules Module

Publicly Accessible Classes:
    Schedule
    UnitSchedule

"""

import datetime

from .base_schedule import Schedule
from .unit import UnitSchedule

__all__ = ["Schedule", "UnitSchedule"]

__title__ = 'schedule'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
