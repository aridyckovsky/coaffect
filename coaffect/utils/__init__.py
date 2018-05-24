# -*- coding: utf-8 -*-
""" Coaffect Utils Module

Utilities are not publicly accessible on the client side.

"""

import datetime

from .trackable_object import TrackableObject
from .state import State

__all__ = ["TrackableObject", "State"]

__title__ = 'utils'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
