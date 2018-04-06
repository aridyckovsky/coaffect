# -*- coding: utf-8 -*-
""" Coaffect Environments Module

Core Objects:
    Environment
    Space
    Time
    Network

"""

import datetime

from .environment import Environment
from .space import Space
from .time import Time
from .network import Network

__all__ = ["Environment", "Space", "Time", "Network"]

__title__ = 'coaffect'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
