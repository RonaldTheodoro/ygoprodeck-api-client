#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import requests


def test_card_data(client_mock):
    assert client_mock.card_data is None
    cards = client_mock.get_all_cards()
    assert isinstance(cards, dict)
    assert client_mock.card_data is not None


def test_get_cards(client_mock, get_payload):
    card = get_payload('test_get_cards.json')

    cards = client_mock.get_cards(name='Meteor B. Dragon')

    assert cards['data'][0] == card


def test_get_cards_misc(client_mock, get_payload):
    payload = get_payload('test_get_cards_misc.json')

    cards = client_mock.get_cards(name='Meteor B. Dragon', misc='yes')

    assert cards['data'][0] == payload


def test_get_random_card(client_mock, get_payload):
    random_cards = get_payload('test_get_random_card.json')

    card_01 = client_mock.get_random_card()
    card_02 = client_mock.get_random_card()
    card_03 = client_mock.get_random_card()

    assert card_01 == random_cards['card_01']
    assert card_02 == random_cards['card_02']
    assert card_03 == random_cards['card_03']


@pytest.mark.skip
def test_get_card_image(client_mock, get_image):
    pass


@pytest.mark.skip
def test_get_card_image_small(client_mock, get_image):
    pass


def test_get_card_sets(client_mock, get_payload):
    card_sets_expected = get_payload('test_get_card_sets.json')
    card_sets = client_mock.get_card_sets()
    assert card_sets == card_sets_expected


def test_get_card_sets_info(client_mock, get_payload):
    card_set_info_expected = get_payload('test_get_card_sets_info.json')
    card_set_info = client_mock.get_card_sets_info('MACR-EN036')
    assert card_set_info == card_set_info_expected


def test_get_archetypes(client_mock, get_payload):
    archtypes_expected = get_payload('test_get_archetypes.json')
    archtypes = client_mock.get_archetypes()
    assert archtypes == archtypes_expected


def test_get_api_database_version(client_mock, get_payload):
    database_version_expected = get_payload(
        'test_get_api_database_version.json'
    )
    database_version = client_mock.get_api_database_version()
    assert database_version == database_version_expected


def test_get_cards_invalid(client_mock):
    with pytest.raises(requests.exceptions.HTTPError):
        client_mock.get_cards(name='Red-Eyes Ultimate Dragon')
