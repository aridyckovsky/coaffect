# -*- coding: utf-8 -*-
""" Coaffect Environments Module

Publicly Accessible Classes:
    Environment
    Space
    Time
    Network
    Group

"""

import datetime

from .base import Environment

from .space import Space
from .time import Time
from .network import Network
from .group import Group

__all__ = ["Environment", "Space", "Time", "Network", "Group"]

__title__ = 'environments'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
