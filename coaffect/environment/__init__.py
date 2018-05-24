# -*- coding: utf-8 -*-
""" Coaffect Environments Module

Publicly Accessible Classes:
    Environment

"""

import datetime

""" The following are imported into environment.py directly

from ..spaces.base import Space
from ..networks.base import Network

"""

from .base_environment import Environment

__all__ = ["Environment"]

__title__ = 'environment'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year