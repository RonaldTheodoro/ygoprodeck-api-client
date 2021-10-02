#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import requests


def test_card_data(client_mock):
    assert client_mock.card_data is None
    cards = client_mock.get_all_cards()
    assert isinstance(cards, dict)
    assert client_mock.card_data is not None


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


def test_get_random_card(client_mock):
    card_01 = client_mock.get_random_card()
    card_02 = client_mock.get_random_card()
    card_03 = client_mock.get_random_card()

    assert card_01 == {
        'id': 22091647,
        'name': 'Immortal Phoenix Gearfried',
        'type': 'Effect Monster',
        'desc': 'You can banish 1 Equip Spell from your field or GY; Special Summon this card from your hand. At the start of the Damage Step, if this card attacks: You can equip 1 face-up monster on the field to this card (max. 1) as an Equip Spell that gives this card 500 ATK. When a monster effect is activated (Quick Effect): You can send 1 face-up Equip Card you control to the GY; negate the activation, and if you do, destroy it. You can only use each effect of "Immortal Phoenix Gearfried" once per turn.',
        'atk': 3000,
        'def': 2200,
        'level': 9,
        'race': 'Warrior',
        'attribute': 'FIRE',
        'card_sets': [
            {
                'set_code': 'TOCH-EN012',
                'set_name': 'Toon Chaos',
                'set_price': '$12.53',
                'set_rarity': "Collector's Rare"
            },
            {
                'set_code': 'TOCH-EN012',
                'set_name': 'Toon Chaos',
                'set_price': '$12.53',
                'set_rarity': 'Ultra Rare'
            }
        ],
        'card_images': [
            {
                'image_url': 'https://storage.googleapis.com/ygoprodeck.com/pics/22091647.jpg',
                'image_url_small': 'https://storage.googleapis.com/ygoprodeck.com/pics_small/22091647.jpg'
            }
        ],
        'card_prices': [
            {
                'amazon_price': '0.82',
                'cardmarket_price': '10.31',
                'ebay_price': '61.00',
                'tcgplayer_price': '10.69'
            }
        ],
    }
    assert card_02 == {
        'id': 77084837,
        'name': 'Inaba White Rabbit',
        'type': 'Spirit Monster',
        'desc': 'This card cannot be Special Summoned. This card returns to the owner\'s hand during the End Phase of the turn that this card is Normal Summoned or flipped face-up. This monster attacks your opponent\'s Life Points directly.',
        'atk': 700,
        'def': 500,
        'level': 3,
        'race': 'Beast',
        'attribute': 'EARTH',
        'card_sets': [
            {
                'set_code': 'DB2-EN176',
                'set_name': 'Dark Beginning 2',
                'set_price': '$3.63',
                'set_rarity': 'Common'
            },
            {
                'set_code': 'LOD-065',
                'set_name': 'Legacy of Darkness',
                'set_price': '$2.67',
                'set_rarity': 'Short Print'
            },
            {
                'set_code': 'LOD-EN065',
                'set_name': 'Legacy of Darkness',
                'set_price': '$5.4',
                'set_rarity': 'Short Print'
            }
        ],
        'card_images': [
            {
                'image_url': 'https://storage.googleapis.com/ygoprodeck.com/pics/77084837.jpg',
                'image_url_small': 'https://storage.googleapis.com/ygoprodeck.com/pics_small/77084837.jpg'
            }
        ],
        'card_prices': [
            {
                'amazon_price': '2.58',
                'cardmarket_price': '0.12',
                'ebay_price': '0.99',
                'tcgplayer_price': '0.93'
            }
        ],
    }
    assert card_03 == {
        'id': 12076263,
        'name': 'Wind-Up Dog',
        'type': 'Effect Monster',
        'desc': 'During your Main Phase: You can increase this card\'s Level by 2 and ATK by 600, until the End Phase. This effect can be used only once while this card is face-up on the field.',
        'atk': 1200,
        'def': 900,
        'level': 3,
        'race': 'Beast',
        'attribute': 'EARTH',
        'archetype': 'Wind-Up',
        'card_images': [
            {
                'image_url': 'https://storage.googleapis.com/ygoprodeck.com/pics/12076263.jpg',
                'image_url_small': 'https://storage.googleapis.com/ygoprodeck.com/pics_small/12076263.jpg'
            }
        ],
        'card_prices': [
            {
                'amazon_price': '1.04',
                'cardmarket_price': '0.06',
                'ebay_price': '0.99',
                'tcgplayer_price': '0.14'
            }
        ],
        'card_sets': [
            {
                'set_code': 'BP01-EN167',
                'set_name': 'Battle Pack: Epic Dawn',
                'set_price': '$1.19',
                'set_rarity': 'Common'
            },
            {
                'set_code': 'BP01-EN167',
                'set_name': 'Battle Pack: Epic Dawn',
                'set_price': '$1.2',
                'set_rarity': 'Starfoil Rare'
            },
            {
                'set_code': 'GENF-EN016',
                'set_name': 'Generation Force',
                'set_price': '$1.08',
                'set_rarity': 'Common'
            }
        ],
    }


def test_get_cards_invalid(client_mock):
    with pytest.raises(requests.exceptions.HTTPError):
        client_mock.get_cards(name='Red-Eyes Ultimate Dragon')
