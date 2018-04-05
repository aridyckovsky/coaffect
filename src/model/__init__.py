# -*- coding: utf-8 -*-
"""

Collective Emotion Modeling Framework

Core Objects: Simulate, Group, Agent

"""

import datetime

from .simulate import Simulate
from .group import Group
from .agent import Agent


__all__ = ["Simulate", "Group", "Agent"]

__title__ = 'collective-emotion'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
