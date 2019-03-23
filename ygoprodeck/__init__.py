#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
YGOPro deck API client
~~~~~~~~~~~~~~~~~~~~~~

This is a simple client for YGOPro deck API.
"""

from .ygoprodeck import YGOProDeck
from . import constants, exceptions


__all__ = ['YGOProDeck', 'constants', 'exceptions']
