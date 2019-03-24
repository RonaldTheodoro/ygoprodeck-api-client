#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from .context import ygoprodeck


@pytest.fixture
def card():
    return ygoprodeck.models.Card()


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
