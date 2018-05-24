# -*- coding: utf-8 -*-
""" Coaffect Groups Module

Publicly Accessible Classes:
    Group
    EmotionalGroup

"""

import datetime

from .base_group import Group
from .emotional import EmotionalGroup

__all__ = ["Group", "EmotionalGroup"]

__title__ = 'group'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
