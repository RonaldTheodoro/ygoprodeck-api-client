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
class CardSet:
    set_name: str
    set_code: str
    set_rarity: str
    set_rarity_code: str
    set_price: str


@dataclass
class CardImage:
    id: int
    image_url: str
    image_url_small: str
    image_url_cropped: str


@dataclass
class CardPrice:
    cardmarket_price: str
    tcgplayer_price: str
    ebay_price: str
    amazon_price: str
    coolstuffinc_price: str


@dataclass
class Card:
    """Model that represent a card instance"""

    id: Optional[int] = None
    name: Optional[str] = None
    _type: Optional[str] = field(default=None)
    desc: Optional[str] = None
    atk: Optional[int] = None
    def_: Optional[int] = None
    _level: Optional[int] = field(default=None)
    _attribute: Optional[str] = field(default=None)
    _scale: Optional[int] = field(default=None)
    _race: Optional[str] = field(default=None)
    archetype: Optional[str] = None

    _link: Optional[int] = field(default=None)
    _linkmarkers: Optional[list[str]] = field(default=None)

    _set_tag: Optional[list[str]] = field(default=None)
    _setcode: Optional[list[str]] = field(default=None)

    image_url: Optional[str] = None
    image_url_small: Optional[str] = None

    _ban_tcg: Optional[str] = field(default=None)
    _ban_ocg: Optional[str] = field(default=None)
    _ban_goat: Optional[str] = field(default=None)

    _card_sets: Optional[list[CardSet]] = None
    _card_images: Optional[list[CardImage]] = None
    _card_prices: Optional[list[CardPrice]] = None

    @property
    def type_(self) -> Optional[str]:
        return self._type

    @type_.setter
    def type_(self, type_: str):
        validators.card_type(type_)
        self._type = type_

    @property
    def level(self) -> Optional[int]:
        return self._level

    @level.setter
    def level(self, level: int):
        if level is not None:
            validators.card_level_rank(level)
        self._level = level

    @property
    def attribute(self) -> Optional[str]:
        return self._attribute

    @attribute.setter
    def attribute(self, attribute: str):
        if attribute is not None:
            validators.card_attribute(attribute)
        self._attribute = attribute

    @property
    def scale(self) -> Optional[int]:
        return self._scale

    @scale.setter
    def scale(self, scale: int):
        if scale is not None:
            validators.card_pendulum_scale(scale)
        self._scale = scale

    @property
    def race(self) -> Optional[str]:
        return self._race

    @race.setter
    def race(self, race: str):
        validators.card_race(race)
        self._race = race

    @property
    def link(self) -> Optional[int]:
        return self._link

    @link.setter
    def link(self, link: int):
        if link is not None:
            validators.card_link(link)
        self._link = link

    @property
    def linkmarkers(self) -> Optional[list[str]]:
        return self._linkmarkers

    @linkmarkers.setter
    def linkmarkers(self, linkmarkers: str):
        if linkmarkers is not None:
            linkmarkers = linkmarkers.split(",")
            if linkmarkers[-1] == "":
                linkmarkers.pop(-1)
            for marker in linkmarkers:
                validators.card_linkmarker(marker)
        self._linkmarkers = linkmarkers

    @property
    def set_tag(self) -> Optional[list[str]]:
        return self._set_tag

    @set_tag.setter
    def set_tag(self, set_tag: str):
        set_tag = set_tag.split(",")
        if set_tag[-1] == "":
            set_tag.pop(-1)
        self._set_tag = set_tag

    @property
    def setcode(self) -> Optional[list[str]]:
        return self._setcode

    @setcode.setter
    def setcode(self, setcode: str):
        setcode = setcode.split(",")
        if setcode[-1] == "":
            setcode.pop(-1)
        self._setcode = setcode

    @property
    def ban_tcg(self) -> Optional[str]:
        return self._ban_tcg

    @ban_tcg.setter
    def ban_tcg(self, ban_tcg: str):
        if ban_tcg is not None:
            validators.card_banlist_status(ban_tcg)
        self._ban_tcg = ban_tcg

    @property
    def ban_ocg(self: str) -> Optional[str]:
        return self._ban_ocg

    @ban_ocg.setter
    def ban_ocg(self, ban_ocg: str) -> Optional[str]:
        if ban_ocg is not None:
            validators.card_banlist_status(ban_ocg)
        self._ban_ocg = ban_ocg

    @property
    def ban_goat(self) -> Optional[str]:
        return self._ban_goat

    @ban_goat.setter
    def ban_goat(self, ban_goat: str):
        if ban_goat is not None:
            validators.card_banlist_status(ban_goat)
        self._ban_goat = ban_goat

    @property
    def card_sets(self) -> Optional[list[CardSet]]:
        return self._card_sets

    @card_sets.setter
    def card_sets(self, card_sets: list):
        self._card_sets = [CardSet(**c) for c in card_sets]

    @property
    def card_images(self) -> Optional[list[CardImage]]:
        return self._card_images

    @card_images.setter
    def card_images(self, card_images: list):
        self._card_images = [CardImage(**c) for c in card_images]

    @property
    def card_prices(self) -> Optional[list[CardPrice]]:
        return self._card_prices

    @card_prices.setter
    def card_prices(self, card_prices: list):
        self._card_prices = [CardPrice(**c) for c in card_prices]
