from . import constants, exceptions


def card_type(card_type):
    if card_type not in constants.TYPES:
        raise exceptions.TypeInvalid()


def card_level_rank(level):
    try:
        level = int(level)
    except ValueError:
        raise exceptions.LevelOrRankInvalid()

    if level not in range(0, 13):
        raise exceptions.LevelOrRankInvalid()


def card_race(race):
    if race not in constants.RACE:
        raise exceptions.RaceInvalid()


def card_attribute(attribute):
    if attribute not in constants.ATTRIBUTES:
        raise exceptions.AttributeInvalid()


def card_link(link):
    try:
        link = int(link)
    except ValueError:
        raise exceptions.LinkRatingInvalid()

    if link not in range(1, 9):
        raise exceptions.LinkRatingInvalid()


def card_linkmarker(linkmarker):
    if linkmarker not in constants.LINK_MARKERS:
        raise exceptions.LinkMarkerInvalid()


def card_pendulum_scale(scale):
    try:
        scale = int(scale)
    except ValueError:
        raise exceptions.PendulumScaleInvalid()

    if scale not in range(0, 14):
        raise exceptions.PendulumScaleInvalid()


def card_banlist(banlist):
    if banlist not in constants.BANLIST:
        raise exceptions.BanlistInvalid()


def card_sort_params(sort):
    if sort not in constants.SORT_PARAMS:
        raise exceptions.SortParamInvalid()


validators = {
    'type': card_type,
    'level': card_level_rank,
    'race': card_race,
    'attribute': card_attribute,
    'link': card_link,
    'linkmarker': card_linkmarker,
    'scale': card_pendulum_scale,
    'banlist': card_banlist,
    'sort': card_sort_params,
}
