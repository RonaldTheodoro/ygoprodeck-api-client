#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pytest
import requests
from betamax import Betamax

from .context import ygoprodeck


WORKERS_DIR = os.path.dirname(os.path.abspath(__file__))
CASSETTES_DIR = os.path.join(WORKERS_DIR, u'resources', u'cassettes')

with Betamax.configure() as config:
    config.cassette_library_dir = CASSETTES_DIR


@pytest.fixture
@pytest.mark.usefixtures('betamax_session')
def client(betamax_session):
    client = ygoprodeck.Client(validate=False)
    client.session = betamax_session
    return client


def test_get_cards(client):
    cards = client.get_cards(name='Meteor B. Dragon')
    expected = {
        'id': '90660762',
        'name': 'Meteor B. Dragon',
        'type': 'Fusion Monster',
        'desc': '"Red-Eyes B. Dragon" + "Meteor Dragon"',
        'atk': '3500',
        'def': '2000',
        'level': '8',
        'race': 'Dragon',
        'attribute': 'FIRE',
        'archetype': 'Red-Eyes',
        'set_tag': 'PRC1-EN004,',
        'setcode': 'Premium Collection Tin,',
        'image_url': (
            'https://storage.googleapis.com/ygoprodeck.com/pics/90660762.jpg'
        ),
        'image_url_small': (
            'https://storage.googleapis.com/ygoprodeck.com/'
            'pics_small/90660762.jpg'
        )
    }
    assert cards[0][0] == expected


def test_get_cards_invalid(client):
    with pytest.raises(requests.exceptions.HTTPError):
        client.get_cards(name='Red-Eyes Ultimate Dragon')
