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

""" The following are imported into environment.py directly

from .features.space import Space
from .features.network import Network

"""

from .base import Environment

__all__ = ["Environment"]

__title__ = 'environments'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
