import pytest

from .context import ygoprodeck


@pytest.fixture
def client():
    return ygoprodeck.YGOProDeck()


def test_validate_type(client):
    with pytest.raises(ygoprodeck.exceptions.TypeInvalid):
        client.get_cards(type_='not valid type')


