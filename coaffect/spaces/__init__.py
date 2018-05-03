# -*- coding: utf-8 -*-
""" Coaffect Spaces Module

Base Class:
    Space

Subclasses:
    Space1D
    Space2D
    Space3D

"""

import datetime

from .base import Space
from .space_1d import Space1D

__all__ = ["Space", "Space1D"]

__title__ = 'spaces'
__version__ = '0.1.0'
__license__ = 'MIT'

__copyright__ = 'Copyright %s Stanford Collective Emotion Team' % datetime.date.today().year
