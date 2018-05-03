# -*- coding: utf-8 -*-
""" Coaffect Core Module

Publicly Accessible Classes:

"""

#: General dependencies
import datetime
import numpy
import scipy

#: Schedules
from .schedules.base import Schedule
from .schedules.unit import UnitSchedule

#: Networks
from .networks.base import Network

#: Spaces
from .spaces.base import Space
from .spaces.space_1d import Space1D

#: Environments
from .environments.base import Environment

#: Agents
from .agents.base import Agent
from .agents.emotional import EmotionalAgent
from .agents.social import SocialEmotionalAgent

#: Groups
from .groups.base import Group

#: Experiments
from .experiments.base import Experiment
from .experiments.simulation import Simulation

#: History
from .history.base import History

__all__ = [
    "Schedule",
    "SimpleSchedule",

    "Environment",
    "Network",
    "Space",

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
