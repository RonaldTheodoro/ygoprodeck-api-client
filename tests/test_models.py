#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from .context import ygoprodeck


def test_model_type(card):
    with pytest.raises(ygoprodeck.exceptions.TypeInvalid):
        card.type_ = 'Not a valid type'


def test_model_level(card):
    with pytest.raises(ygoprodeck.exceptions.LevelOrRankInvalid):
        card.level = 15


def test_model_attribute(card):
    with pytest.raises(ygoprodeck.exceptions.AttributeInvalid):
        card.attribute = 'pyro'


def test_model_pendunlum_scale(card):
    with pytest.raises(ygoprodeck.exceptions.PendulumScaleInvalid):
        card.scale = 15


def test_model_link(card):
    with pytest.raises(ygoprodeck.exceptions.LinkRatingInvalid):
        card.link = 9


def test_model_linkmarkers(card):
    with pytest.raises(ygoprodeck.exceptions.LinkMarkerInvalid):
        card.linkmarkers = 'north'


def test_model_race(card):
    with pytest.raises(ygoprodeck.exceptions.RaceInvalid):
        card.race = 'yokai'


def test_model_ban_tcg(card):
    with pytest.raises(ygoprodeck.exceptions.BanlistStatusInvalid):
        card.ban_tcg = 'status'


def test_model_ban_ocg(card):
    with pytest.raises(ygoprodeck.exceptions.BanlistStatusInvalid):
        card.ban_ocg = 'status'


def test_model_ban_goat(card):
    with pytest.raises(ygoprodeck.exceptions.BanlistStatusInvalid):
        card.ban_goat = 'status'


def test_model_linkmarker_list(card):
    card.linkmarkers = 'left,right,bottom,'
    assert card.linkmarkers == ['left', 'right', 'bottom', ]


def test_model_set_tag(card):
    card.set_tag = 'YS12-EN037,YS11-EN039,LODT-EN063,5DS2-EN037,'
    set_tag = ['YS12-EN037', 'YS11-EN039', 'LODT-EN063', '5DS2-EN037', ]
    assert card.set_tag == set_tag


def test_model_setcode(card):
    card.setcode = 'Raging Tempest,2017 Mega-Tin Mega Pack,'
    setcode = ['Raging Tempest', '2017 Mega-Tin Mega Pack']
    assert card.setcode == setcode


def test_model_card_sets(card):
    card_sets = [
        {
          "set_name": "Battles of Legend: Relentless Revenge",
          "set_code": "BLRR-EN084",
          "set_rarity": "Secret Rare",
          "set_rarity_code": "(ScR)",
          "set_price": "4.08"
        },
        {
          "set_name": "Duel Devastator",
          "set_code": "DUDE-EN019",
          "set_rarity": "Ultra Rare",
          "set_rarity_code": "(UR)",
          "set_price": "1.4"
        },
        {
          "set_name": "Maximum Crisis",
          "set_code": "MACR-EN081",
          "set_rarity": "Secret Rare",
          "set_rarity_code": "(ScR)",
          "set_price": "4.32"
        }
    ]
    card.card_sets = card_sets
    assert len(card.card_sets) == 3
    assert all([
        isinstance(c, ygoprodeck.models.CardSet) for c in card.card_sets
    ])


def test_model_card_images(card):
    card_images = [
        {
          "id": 6983839,
          "image_url": "https://images.ygoprodeck.com/images/cards/6983839.jpg",
          "image_url_small": "https://images.ygoprodeck.com/images/cards_small/6983839.jpg",
          "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/6983839.jpg"
        }
    ]
    card.card_images = card_images
    assert len(card.card_images) == 1
    assert [isinstance(c, ygoprodeck.models.CardImage) for c in card.card_images]


def test_model_card_prices(card):
    card_prices = [
        {
          "cardmarket_price": "0.42",
          "tcgplayer_price": "0.48",
          "ebay_price": "2.99",
          "amazon_price": "0.77",
          "coolstuffinc_price": "0.99"
        }
    ]
    card.card_prices = card_prices
    assert len(card.card_prices) == 1
    assert [isinstance(c, ygoprodeck.models.CardPrice) for c in card.card_prices]