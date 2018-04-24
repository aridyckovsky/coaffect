# -*- coding: utf-8 -*-
""" Coaffect Experiments Module

Base Class:
    Experiment

Subclasses:
    Simulation

"""

import datetime

from .base import Experiment
from .simulation import Simulation

__all__ = ["Experiment", "Simulation"]

__title__ = 'experiments'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
