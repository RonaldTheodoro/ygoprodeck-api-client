#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ygoprodeck.constants
~~~~~~~~~~~~~~~~~~~~

Constant values.
"""

import enum


class EnumMixin(enum.Enum):

    @classmethod
    def is_valid_value(cls, value):
        return any(item.value == value for item in cls)

    @classmethod
    def valid_values(cls):
        return [v.value for n, v in cls.__members__.items()]


class Race(EnumMixin):
    AQUA = 'aqua'
    BEAST = 'beast'
    BEAST_WARRIOR = 'beast-warrior'
    CREATOR_GOD = 'creator-god'
    CYBERSE = 'cyberse'
    DINOSAUR = 'dinosaur'
    DIVINE_BEAST = 'divine-beast'
    DRAGON = 'dragon'
    FAIRY = 'fairy'
    FIEND = 'fiend'
    FISH = 'fish'
    INSECT = 'insect'
    MACHINE = 'machine'
    PLANT = 'plant'
    PSYCHIC = 'psychic'
    PYRO = 'pyro'
    REPTILE = 'reptile'
    ROCK = 'rock'
    SEA_SERPENT = 'sea serpent'
    SPELLCASTER = 'spellcaster'
    THUNDER = 'thunder'
    WARRIOR = 'warrior'
    WINGED_BEAST = 'winged beast'
    NORMAL = 'normal'
    FIELD = 'field'
    EQUIP = 'equip'
    CONTINUOUS = 'continuous'
    QUICK_PLAY = 'quick-play'
    RITUAL = 'ritual'
    COUNTER = 'counter'


class CardTypes(EnumMixin):
    EFFECT_MONSTER = 'effect monster'
    FLIP_EFFECT_MONSTER = 'flip effect monster'
    FLIP_TUNER_EFFECT_MONSTER = 'flip tuner effect monster'
    GEMINI_MONSTER = 'gemini monster'
    NORMAL_MONSTER = 'normal monster'
    NORMAL_TUNER_MONSTER = 'normal tuner monster'
    PENDULUM_EFFECT_FUSION_MONSTER = 'pendulum effect fusion monster'
    PENDULUM_EFFECT_MONSTER = 'pendulum effect monster'
    PENDULUM_FLIP_EFFECT_MONSTER = 'pendulum flip effect monster'
    PENDULUM_NORMAL_MONSTER = 'pendulum normal monster'
    PENDULUM_TUNER_EFFECT_MONSTER = 'pendulum tuner effect monster'
    RITUAL_EFFECT_MONSTER = 'ritual effect monster'
    RITUAL_MONSTER = 'ritual monster'
    SKILL_CARD = 'skill card'
    SPELL_CARD = 'spell card'
    SPIRIT_MONSTER = 'spirit monster'
    TOON_MONSTER = 'toon monster'
    TRAP_CARD = 'trap card'
    TUNER_MONSTER = 'tuner monster'
    UNION_EFFECT_MONSTER = 'union effect monster'
    UNION_TUNER_EFFECT_MONSTER = 'union tuner effect monster'
    FUSION_MONSTER = 'fusion monster'
    LINK_MONSTER = 'link monster'
    SYNCHRO_MONSTER = 'synchro monster'
    SYNCHRO_PENDULUM_EFFECT_MONSTER = 'synchro pendulum effect monster'
    SYNCHRO_TUNER_MONSTER = 'synchro tuner monster'
    XYZ_MONSTER = 'xyz monster'
    XYZ_PENDULUM_EFFECT_MONSTER = 'xyz pendulum effect monster'


class Attributes(EnumMixin):
    DARK = 'dark'
    DIVINE = 'divine'
    EARTH = 'earth'
    FIRE = 'fire'
    LIGHT = 'light'
    WATER = 'water'
    WIND = 'wind'


class Language(EnumMixin):
    ENGLISH = 'en'
    FRENCH = 'fr'
    GERMAN = 'de'
    PORTUGUESE = 'pt'
    ITALIAN = 'it'


class LinkMarkers(EnumMixin):
    TOP = 'top'
    TOP_RIGHT = 'top-right'
    TOP_LEFT = 'top-left'
    LEFT = 'left'
    RIGHT = 'right'
    BOTTOM = 'bottom'
    BOTTOM_RIGHT = 'bottom-right'
    BOTTOM_LEFT = 'bottom-left'


class Banlist(EnumMixin):
    TCG = 'tcg'
    OCG = 'ocg'
    GOAT = 'goat'


class BanlistStatus(EnumMixin):
    BANNED = 'banned'
    LIMITED = 'limited'
    SEMI_LIMITED = 'semi-limited'
    UNLIMITED = 'unlimited'


class SortParams(EnumMixin):
    ATK = 'atk'
    DEF = 'def'
    NAME = 'name'
    TYPE = 'type'
    LEVEL = 'level'
    ID = 'id'
    NEW = 'new'


class Format(EnumMixin):
    TCG = 'tcg'
    GOAT = 'goat'
    OCG_GOAT = 'ocg goat'
    SPEED_DUEL = 'speed duel'
    RUSH_DUEL = 'rush duel'
    DUEL_LINKS = 'duel links'
