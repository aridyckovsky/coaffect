# -*- coding: utf-8 -*-
""" Coaffect Participants Module

Core Objects:
    Agent
    Group

"""

import datetime

from .group import Group
from .agent import Agent

__all__ = ["Group", "Agent"]

__title__ = 'coaffect'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
