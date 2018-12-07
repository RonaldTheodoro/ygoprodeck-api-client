

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
