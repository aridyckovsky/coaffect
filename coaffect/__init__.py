# -*- coding: utf-8 -*-
""" Coaffect Core Module

Publicly Accessible Classes:

"""

#: General dependencies
import datetime
import numpy
import scipy

#: Schedules
from .schedule.base_schedule import Schedule
from .schedule.unit import UnitSchedule

#: Networks
from .network.base_network import Network

#: Spaces
from .space.base_space import Space

#: Environments
from .environment.base_environment import Environment

#: Resources
from .resource.base_resource import Resource

#: Agents
from .agent.base_agent import Agent
from .agent.emotional import EmotionalAgent
from .agent.spatial import SpatialAgent
from .agent.remembering import RememberingAgent

#: Groups
from .group.base_group import Group
from .group.emotional import EmotionalGroup

#: Experiments
from .simulation.base_simulation import Simulation

#: History
from .history.base_history import History

__all__ = [
    "Schedule",
    "SimpleSchedule",

    "Environment",
    "Network",
    "Space",
    "Resource",

    "Agent",
    "EmotionalAgent",
    "SpatialAgent",
    "RememberingAgent",

    "Group",
    "EmotionalGroup",

    "Simulation",

    "History",

    "State"
]

__title__ = 'coaffect'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
