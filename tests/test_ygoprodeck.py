import pytest

from .context import ygoprodeck


@pytest.fixture
def client():
    return ygoprodeck.YGOProDeck()


def test_validate_type(client):
    with pytest.raises(ygoprodeck.exceptions.TypeInvalid):
        client.get_cards(type_='not valid type')


def test_validate_level_rank_invalid_value(client):
    with pytest.raises(ygoprodeck.exceptions.LevelOrRankInvalid):
        client.get_cards(level='not a number')


def test_validate_level_rank_out_of_range(client):
    with pytest.raises(ygoprodeck.exceptions.LevelOrRankInvalid):
        client.get_cards(level=15)
