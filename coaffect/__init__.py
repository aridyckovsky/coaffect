# -*- coding: utf-8 -*-
""" Coaffect Core Module

Publicly Accessible Classes:

"""

#: General dependencies
import datetime
import numpy
import scipy

#: Time and Schedules
from .schedules.base import Schedule
from .schedules.unit import UnitSchedule

#: Environments
from .environments.base import Environment

#: Agents
from .agents.base import Agent
from .agents.emotional import EmotionalAgent

#: Groups
from .groups.base import Group

#: Experiments
from .experiments.base import Experiment
from .experiments.simulation import Simulation

#: History
from .history.base import History

#: States
from .states.base import State

__all__ = [
    "Schedule",
    "SimpleSchedule",

    "Environment",

    "Agent",
    "EmotionalAgent",

    "Group",

    "Experiment",
    "Simulation",

    "History",

    "State"
]

__title__ = 'coaffect'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
