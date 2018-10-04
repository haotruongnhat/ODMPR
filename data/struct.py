"""Defines data structure."""
from collections import namedtuple


MarkingPoint = namedtuple('MarkingPoint', ['x', 'y', 'direction', 'shape'])
Slot = namedtuple('Slot', ['x1', 'y1', 'x2', 'y2'])
