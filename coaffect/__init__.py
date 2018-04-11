# -*- coding: utf-8 -*-
""" Coaffect Core Module

Publicly Accessible Classes:

    Agent -- Reminder that this is temporary for development needs
    EmotionalAgent

    Environment
    Group

"""

import datetime

from .participants import Agent
from .participants import EmotionalAgent

from .environments import Environment
from .environments import Group

__all__ = [
    "Agent",
    "EmotionalAgent",

    "Environment",
    "Group"
]

__title__ = 'coaffect'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
