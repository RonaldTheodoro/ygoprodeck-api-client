

class YGOProDeckException(Exception):
    pass


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
