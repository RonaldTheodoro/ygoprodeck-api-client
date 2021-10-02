#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ygoprodeck.validators
~~~~~~~~~~~~~~~~~~~~

Functions to validate the parameters before make a request.
"""


from . import constants, exceptions


def remove_underline(params):
    """Remove the underline in reserved words.

    The parameters def and type are python reserved words so it is necessary
    to add a underline to use this words, this method remove the underline
    before make a http request.

    Args:
        params (dict): Url query parameters.

    Returns:
        (dict): Validated url query parameters.
    """
    modified_params = {'def_': 'def', 'type_': 'type', 'format_': 'format'}

    for key, value in modified_params.items():
        if key in params.keys():
            param_value = params.pop(key)
            params[value] = param_value

    return params


def card_id_and_name(params):
    """Check if id and name are passed in the same requests
    Args:
        params (dict): Request params.

    Raises:
        exceptions.IdNameError: Id and name cannot be passed in the same
            request.

    """
    if 'name' in params and 'id' in params:
        raise exceptions.IdNameError()


def card_type(card_type):
    """Validate card type.

    Args:
        card_type (str): Card type.

    Raises:
        exceptions.TypeInvalid: Card type is not valid.
    """
    if not constants.CardTypes.is_valid_value(card_type):
        raise exceptions.TypeInvalid()


def card_level_rank(level):
    """Validate card level or rank.

    Args:
        level (int): Card level or rank.

    Raises:
        exceptions.LevelOrRankInvalid: Level or rank must be a integer
            between 0 and 12.
    """
    try:
        level = int(level)
    except ValueError:
        raise exceptions.LevelOrRankInvalid()

    if level not in range(0, 13):
        raise exceptions.LevelOrRankInvalid()


def card_race(race):
    """Validate card race.

    Args:
        race (str): Card race.

    Raises:
        exceptions.RaceInvalid: Card race do not exists.
    """
    if not constants.Race.is_valid_value(race):
        raise exceptions.RaceInvalid()


def card_attribute(attribute):
    """Validate card attribute.

    Args:
        attribute (str): Card attribute.

    Raises:
        exceptions.AttributeInvalid: Card attribute do not exists.
    """
    if not constants.Attributes.is_valid_value(attribute):
        raise exceptions.AttributeInvalid()


def card_link(link):
    """Validate card link rating.

    Args:
        link (int): Card link rating.

    Raises:
        exceptions.LinkRatingInvalid: Link rating must be a integer
            between 1 and 8.
    """
    try:
        link = int(link)
    except ValueError:
        raise exceptions.LinkRatingInvalid()

    if link not in range(1, 9):
        raise exceptions.LinkRatingInvalid()


def card_linkmarker(linkmarker):
    """Validate card link marker.

    Args:
        linkmarker (str): Card link marker.

    Raises:
        exceptions.LinkMarkerInvalid: Link marker do not exists.
    """
    if not constants.LinkMarkers.is_valid_value(linkmarker):
        raise exceptions.LinkMarkerInvalid()


def card_pendulum_scale(scale):
    """Validate pendulum scale.

    Args:
        scale (int): Card pendulum scale.

    Raises:
        exceptions.PendulumScaleInvalid: Pendulum scale must be a integer
            between 0 and 13.
    """
    try:
        scale = int(scale)
    except ValueError:
        raise exceptions.PendulumScaleInvalid()

    if scale not in range(0, 14):
        raise exceptions.PendulumScaleInvalid()


def card_banlist(banlist):
    """Validate banlist.

    Args:
        banlist (str): Banlist name.

    Raises:
        exceptions.BanlistInvalid: Banlist must be TCG, OCG or Goat.
    """
    if not constants.Banlist.is_valid_value(banlist):
        raise exceptions.BanlistInvalid()


def card_sort_params(sort):
    """Validate sort parameters.

    Args:
        sort (str): Sort parameters.

    Raises:
        exceptions.SortParamInvalid: Sort parameters must be atk, def, name,
            type, level, id or new.
    """
    if not constants.SortParams.is_valid_value(sort):
        raise exceptions.SortParamInvalid()


def card_banlist_status(banlist_status):
    """Validate banlist status

    Args:
        banlist_status {str}: Banlist status

    Raises:
        exceptions.BanlistStatusInvalid: Banlist status must be banned,
            limited, semi-limited or unlimited
    """

    if not constants.BanlistStatus.is_valid_value(banlist_status):
        raise exceptions.BanlistStatusInvalid()

def card_format(card_format):
    """Validate format status

    Args:
        card_format {str}: Card format

    Raises:
        exceptions.CardFormatInvalid: Banlist status must be banned,
            limited, semi-limited or unlimited
    """
    if not constants.Format.is_valid_value(card_format):
        raise exceptions.CardFormatInvalid()


def card_has_effect(has_effect):
    """Validate has_effect

    Args:
        has_effect {bool}: has effect

    Raises:
        exceptions.HasEffectInvalid: has effect must be a boolean
    """
    if not isinstance(has_effect, bool):
        raise exceptions.HasEffectInvalid()

def card_language(language):
    """Validate language

    Args:
        language {str}: language

    Raises:
        exceptions.LanguageInvalid: No valid language set. This API accepts the
            following language values: 'fr', 'de', 'it' or 'pt' which are
            respectively 'French', 'German', 'Italian' or 'Portuguese'.
            For English, please exclude passing language altogether.
    """
    if not constants.Language.is_valid_value(language):
        raise exceptions.LanguageInvalid()


validators = {
    'type': card_type,
    'level': card_level_rank,
    'race': card_race,
    'attribute': card_attribute,
    'link': card_link,
    'linkmarker': card_linkmarker,
    'scale': card_pendulum_scale,
    'banlist': card_banlist,
    'banlist_status': card_banlist_status,
    'sort': card_sort_params,
    'format': card_format,
    'has_effect': card_has_effect,
    'language': card_language,
}
