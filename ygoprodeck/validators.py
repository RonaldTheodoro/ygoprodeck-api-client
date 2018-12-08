from . import constants, exceptions


def card_type(card_type):
    if card_type is not None:
        if card_type.lower() not in constants.TYPES:
            raise exceptions.TypeInvalid()


def card_level_rank(level):
    if level is not None:
        try:
            level = int(level)
        except ValueError:
            raise exceptions.LevelOrRankInvalid()

        if level not in range(0, 13):
            raise exceptions.LevelOrRankInvalid()


def card_race(race):
    if race is not None:
        if race.lower() not in constants.RACE:
            raise exceptions.RaceInvalid()


def card_attribute(attribute):
    if attribute is not None:
        if attribute.lower() not in constants.ATTRIBUTES:
            raise exceptions.AttributeInvalid()


def card_link(link):
    if link is not None:
        try:
            link = int(link)
        except ValueError:
            raise exceptions.LinkRatingInvalid()

        if link not in range(1, 9):
            raise exceptions.LinkRatingInvalid()


def card_linkmarker(linkmarker):
     if linkmarker is not None:
        if linkmarker.lower() not in constants.LINK_MARKERS:
            raise exceptions.LinkMarkerInvalid()


def card_pendulum_scale(scale):
    if scale is not None:
        try:
            scale = int(scale)
        except ValueError:
            raise exceptions.PendulumScaleInvalid()

        if scale not in range(0, 14):
            raise exceptions.PendulumScaleInvalid()


def card_banlist(banlist):
    if banlist is not None:
        if banlist.lower() not in constants.BANLIST:
            raise exceptions.BanlistInvalid()


def card_sort_params(sort):
    if sort is not None:
        if sort.lower() not in constants.SORT_PARAMS:
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
