#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from .context import ygoprodeck


def test_validate_type(client):
    with pytest.raises(ygoprodeck.exceptions.TypeInvalid):
        client.get_cards(type_='not valid type')


def test_validate_level_rank_invalid_value(client):
    with pytest.raises(ygoprodeck.exceptions.LevelOrRankInvalid):
        client.get_cards(level='not a number')


def test_validate_level_rank_out_of_range(client):
    with pytest.raises(ygoprodeck.exceptions.LevelOrRankInvalid):
        client.get_cards(level=15)


def test_validate_race(client):
    with pytest.raises(ygoprodeck.exceptions.RaceInvalid):
        client.get_cards(race='Not a valid race')


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


def test_validate_sort_params(client):
    with pytest.raises(ygoprodeck.exceptions.SortParamInvalid):
        client.get_cards(sort='A invalid parameter')


def test_card_banlist_status():
    with pytest.raises(ygoprodeck.exceptions.BanlistStatusInvalid):
        ygoprodeck.validators.card_banlist_status('banlist')


def test_validate_card_format(client):
    with pytest.raises(ygoprodeck.exceptions.CardFormatInvalid):
        client.get_cards(format_='A not valid format')


def test_remove_underline():
    params = {'atk': 3000, 'def_': 2100, 'type_': 'normal monster'}
    params_expected = {'atk': 3000, 'def': 2100, 'type': 'normal monster'}

    params_modified = ygoprodeck.validators.remove_underline(params)

    assert params_modified == params_expected
