# -*- coding: utf-8 -*-
""" Coaffect Core Module

Publicly Accessible Classes:

    Agent -- Reminder that this is temporary for development needs
    EmotionalAgent

    Environment
    Group

"""

#: General dependencies
import datetime

#: Experiments
from .experiments.base import Experiment
from .experiments.simulation import Simulation

#: Participants
from .participants.base import Agent
from .participants.emotional import EmotionalAgent

#: Environments
from .environments.base import Environment
from .environments.group import Group

#: Records
from .records.base import Record

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
