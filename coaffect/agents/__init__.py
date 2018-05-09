# -*- coding: utf-8 -*-
""" Coaffect Agents Module

Publicly Accessible Classes:
    Agent
    EmotionalAgent
    SpatialAgent
    RememberingAgent

"""

import datetime

from .base import Agent
from .emotional import EmotionalAgent
from .spatial import SpatialAgent
from .remembering import RememberingAgent

__all__ = ["Agent", "EmotionalAgent", "SpatialAgent", "RememberingAgent"]

__title__ = 'agents'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
