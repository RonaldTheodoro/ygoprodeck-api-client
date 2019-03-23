#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ygoprodeck.models
~~~~~~~~~~~~~~~~~~~~~

This module contains the models used in the package.
"""

from . import validators


class Card:
    """Model that represent a card instance"""

    def __init__(self):
        self._id = None
        self._name = None
        self._type = None
        self._desc = None
        self._atk = None
        self._def = None
        self._level = None
        self._attribute = None
        self._scale = None
        self._race = None
        self._archetype = None
        self._link = None
        self._linkmarkers = None
        self._set_tag = None
        self._setcode = None
        self._image_url = None
        self._image_url_small = None
        self._ban_tcg = None
        self._ban_ocg = None
        self._ban_goat = None

    @property
    def id(self):
        """Gets the card id.

        Returns:
            str: Card id.
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Card.

        Args:
            id (int): Card id.
        """
        self._id = id

    @property
    def name(self):
        """Gets the card name.

        Returns:
            str: Card name.
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Card.

        Args:
            name (str): Card name.
        """
        self._name = name

    @property
    def type_(self):
        """Gets the card type.

        Returns:
            str: Card type.
        """
        return self._type

    @type_.setter
    def type_(self, type_):
        """Sets the type of this Card.

        Args:
            type (str): Card type.
        """
        validators.card_type(type_)
        self._type = type_

    @property
    def desc(self):
        """Gets the card description.

        Returns:
            str: Card description.
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the description of this Card.

        Args:
            desc (str): Card description.
        """
        self._desc = desc

    @property
    def atk(self):
        """Gets the card attack.

        Returns:
            int: Card attack.
        """
        return self._atk

    @atk.setter
    def atk(self, atk):
        """Sets the attack of this Card.

        Args:
            atk (int): Card attack.
        """
        self._atk = atk

    @property
    def def_(self):
        """Gets the card defence.

        Returns:
            int: Card defence.
        """
        return self._def

    @def_.setter
    def def_(self, def_):
        """Sets the defence of this Card.

        Args:
            def_ (int): Card defence.
        """
        self._def = def_

    @property
    def level(self):
        """Gets the card level or rank if it is a xyz.

        Returns:
            int: Card level or rank.
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level or rank of this Card.

        Args:
            level (int): Card level or rank.
        """
        if level is not None:
            validators.card_level_rank(level)
        self._level = level

    @property
    def attribute(self):
        """Gets the card attribute.

        Returns:
            str: Card attribute.
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this Card.

        Args:
            attribute (str): Card attribute.
        """
        if attribute is not None:
            validators.card_attribute(attribute)
        self._attribute = attribute

    @property
    def scale(self):
        """Gets the card pendulum scale.

        Returns:
            int: Card pendulum scale.
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the pendulum scale of this Card.

        Args:
            scale (str): Card pendulum scale.
        """
        if scale is not None:
            validators.card_pendulum_scale(scale)
        self._scale = scale

    @property
    def link(self):
        """Gets the card link rating.

        Returns:
            int: Card link rating.
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link rating of this Card.

        Args:
            link (str): Card link rating.
        """
        if link is not None:
            validators.card_link(link)
        self._link = link

    @property
    def linkmarkers(self):
        """Gets the card link markers.

        Returns:
            str: Card link markers.
        """
        return self._linkmarkers

    @linkmarkers.setter
    def linkmarkers(self, linkmarkers):
        """Sets the link markers of this Card.

        Args:
            link (list[str]): Card link markers.
        """
        if linkmarkers is not None:
            linkmarkers = linkmarkers.split(',')
            if linkmarkers[-1] == '':
                linkmarkers.pop(-1)
            for marker in linkmarkers:
                validators.card_linkmarker(marker)
        self._linkmarkers = linkmarkers

    @property
    def race(self):
        """Gets the card race.

        Returns:
            str: Card race.
        """
        return self._race

    @race.setter
    def race(self, race):
        """Sets the race of this Card.

        Args:
            race (str): Card race.
        """
        validators.card_race(race)
        self._race = race

    @property
    def archetype(self):
        """Gets the card archetype.

        Returns:
            int: Card link archetype.
        """
        return self._archetype

    @archetype.setter
    def archetype(self, archetype):
        """Sets the archetype of this Card.

        Args:
            archetype (str): Card archetype.
        """
        self._archetype = archetype

    @property
    def set_tag(self):
        """Gets the card set code.

        Returns:
            list[str]: Card set code.
        """
        return self._set_tag

    @set_tag.setter
    def set_tag(self, set_tag):
        """Sets the set code of this Card.

        Args:
            set_code (str): Card set code.
        """
        set_tag = set_tag.split(',')
        if set_tag[-1] == '':
            set_tag.pop(-1)
        self._set_tag = set_tag

    @property
    def setcode(self):
        """Gets the card boosters.

        Returns:
            list[str]: Card boosters.
        """
        return self._setcode

    @setcode.setter
    def setcode(self, setcode):
        """Sets the boosters of this Card.

        Args:
            setcode (str): Card boosters.
        """
        setcode = setcode.split(',')
        if setcode[-1] == '':
            setcode.pop(-1)
        self._setcode = setcode

    @property
    def image_url(self):
        """Gets the card image url.

        Returns:
            str: Card image url.
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image url of this Card.

        Args:
            image_url (str): Card image.
        """
        self._image_url = image_url

    @property
    def image_url_small(self):
        """Gets the card image url small size.

        Returns:
            str: Card image url small size.
        """
        return self._image_url_small

    @image_url_small.setter
    def image_url_small(self, image_url_small):
        """Sets the small size image url of this Card.

        Args:
            image_url_small (str): Card image url small size.
        """
        self._image_url_small = image_url_small

    @property
    def ban_tcg(self):
        """Gets the card status in the TCG banlist.

        Returns:
            str: Card image status in the TCG banlist.
        """
        return self._ban_tcg

    @ban_tcg.setter
    def ban_tcg(self, ban_tcg):
        """Sets the TCG banlist status of this card.

        Args:
            ban_tcg (str): Card TCG banlist status
        """
        if ban_tcg is not None:
            validators.card_banlist_status(ban_tcg)
        self._ban_tcg = ban_tcg

    @property
    def ban_ocg(self):
        """Gets the card status in the OCG banlist.

        Returns:
            str: Card image status in the OCG banlist.
        """
        return self._ban_ocg

    @ban_ocg.setter
    def ban_ocg(self, ban_ocg):
        """Sets the OCG banlist status of this card.

        Args:
            ban_ocg (str): Card OCG banlist status
        """
        if ban_ocg is not None:
            validators.card_banlist_status(ban_ocg)
        self._ban_ocg = ban_ocg

    @property
    def ban_goat(self):
        """Gets the card status in the GOAT banlist.

        Returns:
            str: Card image status in the GOAT banlist.
        """
        return self._ban_goat

    @ban_goat.setter
    def ban_goat(self, ban_goat):
        """Sets the GOAT banlist status of this card.

        Args:
            ban_goat (str): Card GOAT banlist status
        """
        if ban_goat is not None:
            validators.card_banlist_status(ban_goat)
        self._ban_goat = ban_goat

    def __repr__(self):
        attrs = []
        for k, v in self.__dict__.items():
            if v is not None:
                attrs.append('{k}={v}'.format(k=k.strip('_'), v=v))
        return 'Card({attrs})'.format(attrs=', '.join(attrs))
