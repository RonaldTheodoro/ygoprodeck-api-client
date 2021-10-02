#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import requests


def test_get_cards(client_mock):
    cards = client_mock.get_cards(name='Meteor B. Dragon')
    expected = {
        'id': 90660762,
        'name': 'Meteor Black Dragon',
        'type': 'Fusion Monster',
        'desc': '"Red-Eyes Black Dragon" + "Meteor Dragon"',
        'atk': 3500,
        'def': 2000,
        'level': 8,
        'race': 'Dragon',
        'attribute': 'FIRE',
        'archetype': 'Red-Eyes',
        'card_sets': [
            {
                'set_name': 'Legendary Duelists: Season 1',
                'set_code': 'LDS1-EN013',
                'set_rarity': 'Common',
                'set_rarity_code': '(C)',
                'set_price': '1.06'
            },
            {
                'set_name': 'Premium Collection Tin',
                'set_code': 'PRC1-EN004',
                'set_rarity': 'Super Rare',
                'set_rarity_code': '(SR)',
                'set_price': '4.16'
            },
            {
                'set_name': 'Speed Duel: Arena of Lost Souls',
                'set_code': 'SBLS-EN013',
                'set_rarity': 'Super Rare',
                'set_rarity_code': '(SR)',
                'set_price': '3.59'
            }
        ],
        'card_images': [
            {
                'id': 90660762,
                'image_url': (
                    'https://storage.googleapis.com'
                    '/ygoprodeck.com/pics/90660762.jpg'
                ),
                'image_url_small': (
                    'https://storage.googleapis.com'
                    '/ygoprodeck.com/pics_small/90660762.jpg'
                )
            }
        ],
        'card_prices': [
            {
                'cardmarket_price': '0.14',
                'tcgplayer_price': '1.73',
                'ebay_price': '9.95',
                'amazon_price': '34.99',
                'coolstuffinc_price': '0.25'
            }
        ]
    }
    assert cards['data'][0] == expected


def test_get_cards_misc(client_mock):
    cards = client_mock.get_cards(name='Meteor B. Dragon', misc='yes')
    expected = {
        'id': 90660762,
        'name': 'Meteor Black Dragon',
        'type': 'Fusion Monster',
        'desc': '"Red-Eyes Black Dragon" + "Meteor Dragon"',
        'atk': 3500,
        'def': 2000,
        'level': 8,
        'race': 'Dragon',
        'attribute': 'FIRE',
        'archetype': 'Red-Eyes',
        'card_sets': [
            {
                'set_name': 'Legendary Duelists: Season 1',
                'set_code': 'LDS1-EN013',
                'set_rarity': 'Common',
                'set_rarity_code': '(C)',
                'set_price': '1.06'
            },
            {
                'set_name': 'Premium Collection Tin',
                'set_code': 'PRC1-EN004',
                'set_rarity': 'Super Rare',
                'set_rarity_code': '(SR)',
                'set_price': '4.16'
            },
            {
                'set_name': 'Speed Duel: Arena of Lost Souls',
                'set_code': 'SBLS-EN013',
                'set_rarity': 'Super Rare',
                'set_rarity_code': '(SR)',
                'set_price': '3.59'
            }
        ],
        'card_images': [
            {
                'id': 90660762,
                'image_url': (
                    'https://storage.googleapis.com'
                    '/ygoprodeck.com/pics/90660762.jpg'
                ),
                'image_url_small': (
                    'https://storage.googleapis.com'
                    '/ygoprodeck.com/pics_small/90660762.jpg'
                )
            }
        ],
        'card_prices': [
            {
                'cardmarket_price': '0.14',
                'tcgplayer_price': '1.73',
                'ebay_price': '9.95',
                'amazon_price': '34.99',
                'coolstuffinc_price': '0.25'
            }
        ],
        'misc_info': [
            {
                'beta_name': 'Meteor B. Dragon',
                'downvotes': 1,
                'formats': [
                    'OCG GOAT',
                    'Speed Duel',
                    'Duel Links',
                    'TCG',
                    'OCG'
                ],
                'konami_id': 4719,
                'ocg_date': '1999-08-26',
                'tcg_date': '2012-03-16',
                'upvotes': 28,
                'views': 52284,
                'viewsweek': 195
            }
        ]
    }
    assert cards['data'][0] == expected


def test_get_cards_invalid(client_mock):
    with pytest.raises(requests.exceptions.HTTPError):
        client_mock.get_cards(name='Red-Eyes Ultimate Dragon')
