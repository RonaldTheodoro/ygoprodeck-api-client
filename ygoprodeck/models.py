#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ygoprodeck.models
~~~~~~~~~~~~~~~~~~~~~

This module contains the models used in the package.
"""

from dataclasses import dataclass, field
from typing import Optional

from . import validators


@dataclass
class Card(object):
    """Model that represent a card instance"""

    id: Optional[int] = None
    name: Optional[str] = None
    _type: Optional[str] = field(default=None)
    desc: Optional[str] = None
    atk: Optional[int] = None
    def_: Optional[int] = None
    _level: Optional[int] = field(default=None)
    _attribute: Optional[str] = field(default=None)
    _scale: Optional[str] = field(default=None)
    _race: Optional[str] = field(default=None)
    archetype: Optional[str] = None
    _link: Optional[str] = field(default=None)
    _linkmarkers: Optional[str] = field(default=None)
    _set_tag: Optional[str] = field(default=None)
    _setcode: Optional[str] = field(default=None)
    image_url: Optional[str] = None
    image_url_small: Optional[str] = None
    _ban_tcg: Optional[str] = field(default=None)
    _ban_ocg: Optional[str] = field(default=None)
    _ban_goat: Optional[str] = field(default=None)

    @property
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, type_):
        validators.card_type(type_)
        self._type = type_

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level is not None:
            validators.card_level_rank(level)
        self._level = level

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        if attribute is not None:
            validators.card_attribute(attribute)
        self._attribute = attribute

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, scale):
        if scale is not None:
            validators.card_pendulum_scale(scale)
        self._scale = scale

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        validators.card_race(race)
        self._race = race

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        if link is not None:
            validators.card_link(link)
        self._link = link

    @property
    def linkmarkers(self):
        return self._linkmarkers

    @linkmarkers.setter
    def linkmarkers(self, linkmarkers):
        if linkmarkers is not None:
            linkmarkers = linkmarkers.split(",")
            if linkmarkers[-1] == "":
                linkmarkers.pop(-1)
            for marker in linkmarkers:
                validators.card_linkmarker(marker)
        self._linkmarkers = linkmarkers

    @property
    def set_tag(self):
        return self._set_tag

    @set_tag.setter
    def set_tag(self, set_tag):
        set_tag = set_tag.split(",")
        if set_tag[-1] == "":
            set_tag.pop(-1)
        self._set_tag = set_tag

    @property
    def setcode(self):
        return self._setcode

    @setcode.setter
    def setcode(self, setcode):
        setcode = setcode.split(",")
        if setcode[-1] == "":
            setcode.pop(-1)
        self._setcode = setcode

    @property
    def ban_tcg(self):
        return self._ban_tcg

    @ban_tcg.setter
    def ban_tcg(self, ban_tcg):
        if ban_tcg is not None:
            validators.card_banlist_status(ban_tcg)
        self._ban_tcg = ban_tcg

    @property
    def ban_ocg(self):
        return self._ban_ocg

    @ban_ocg.setter
    def ban_ocg(self, ban_ocg):
        if ban_ocg is not None:
            validators.card_banlist_status(ban_ocg)
        self._ban_ocg = ban_ocg

    @property
    def ban_goat(self):
        return self._ban_goat

    @ban_goat.setter
    def ban_goat(self, ban_goat):
        if ban_goat is not None:
            validators.card_banlist_status(ban_goat)
        self._ban_goat = ban_goat
