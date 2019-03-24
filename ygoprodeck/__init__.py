#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
YGOPro deck API client
~~~~~~~~~~~~~~~~~~~~~~

This is a simple client for YGOPro deck API.
"""

from .client import Client
from . import constants, exceptions, models


__all__ = ['Client', 'constants', 'exceptions', 'models', ]
