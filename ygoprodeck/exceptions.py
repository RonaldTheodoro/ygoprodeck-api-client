#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ygoprodeck.exceptions
~~~~~~~~~~~~~~~~~~~~~

This module contains the set of exceptions used in this package.
"""


class YGOProDeckException(Exception):
    pass


class IdNameError(YGOProDeckException):
    message = 'Id and name cannot be passed in the same request'


class TypeInvalid(YGOProDeckException):
    message = 'Card type is not valid'


class LevelOrRankInvalid(YGOProDeckException):
    message = 'Level or rank must be a integer between 0 and 12'


class RaceInvalid(YGOProDeckException):
    message = 'Card race not exists'


class AttributeInvalid(YGOProDeckException):
    message = 'Card attribute not exists'


class LinkRatingInvalid(YGOProDeckException):
    message = 'Link rating must be a integer between 1 and 8'


class LinkMarkerInvalid(YGOProDeckException):
    message = 'Link marker not exists'


class PendulumScaleInvalid(YGOProDeckException):
    message = 'Pendulum scale must be a integer between 0 and 13'


class BanlistInvalid(YGOProDeckException):
    message = 'Banlist must be TCG, OCG or Goat'


class SortParamInvalid(YGOProDeckException):
    message = 'Sort parameters must be atk, def, name, type, level, id or new'


class BanlistStatusInvalid(YGOProDeckException):
    message = (
        'Banlist status must be banned, limited, semi-limited or unlimited'
    )


class CardFormatInvalid(YGOProDeckException):
    message = (
        'Card format must be tcg, goat, ocg goat, speed duel, '
        'rush duel or duel links'
    )


class HasEffectInvalid(YGOProDeckException):
    message = 'has effect must be a boolean'


class LanguageInvalid(YGOProDeckException): 
    message = (
        "No valid language set. This API accepts the following language "
        "values: 'fr', 'de', 'it' or 'pt' which are respectively 'French', "
        "'German', 'Italian' or 'Portuguese'. For English, please exclude "
        "passing language altogether."
    )
