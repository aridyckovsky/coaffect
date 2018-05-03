# -*- coding: utf-8 -*-
""" Coaffect Agents Module

Publicly Accessible Classes:
    Agent
    EmotionalAgent
    SocialEmotionalAgent

"""

import datetime

from .base import Agent
from .emotional import EmotionalAgent
from .social import SocialEmotionalAgent

__all__ = ["Agent", "EmotionalAgent", "SocialEmotionalAgent"]

__title__ = 'agents'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
