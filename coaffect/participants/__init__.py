# -*- coding: utf-8 -*-
""" Coaffect Participants Module

Publicly Accessible Classes:
    Agent
    EmotionalAgent

"""

import datetime

from .base import Agent
from .emotional import EmotionalAgent

__all__ = ["Agent", "EmotionalAgent"]

__title__ = 'participants'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
