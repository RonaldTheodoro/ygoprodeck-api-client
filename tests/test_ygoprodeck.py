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


def test_validate_attribute(client):
    with pytest.raises(ygoprodeck.exceptions.AttributeInvalid):
        client.get_cards(attribute='Not a valid attribute')


def test_validate_link_invalid_value(client):
    with pytest.raises(ygoprodeck.exceptions.LinkRatingInvalid):
        client.get_cards(link='Not a valid link')


def test_validate_link_out_of_range(client):
    with pytest.raises(ygoprodeck.exceptions.LinkRatingInvalid):
        client.get_cards(link=15)


def test_validate_linkmarker(client):
    with pytest.raises(ygoprodeck.exceptions.LinkMarkerInvalid):
        client.get_cards(linkmarker='North')


def test_validate_pendulum_scale_invalid_value(client):
    with pytest.raises(ygoprodeck.exceptions.PendulumScaleInvalid):
        client.get_cards(scale='Not a number')


def test_validate_pendulum_scale_out_of_range(client):
    with pytest.raises(ygoprodeck.exceptions.PendulumScaleInvalid):
        client.get_cards(scale=-1)


def test_validate_banlist(client):
    with pytest.raises(ygoprodeck.exceptions.BanlistInvalid):
        client.get_cards(banlist='Ban firewall')


def test_change_defense_param_key(client):
    params = client.change_defense_param_key({'def_': 2500})
    assert params == {'def': 2500}


def test_change_type_param_key(client):
    params = client.change_type_param_key({'type_': 'Effect Monster'})
    assert params == {'type': 'Effect Monster'}
