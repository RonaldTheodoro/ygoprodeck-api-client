#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ygoprodeck.YGOProDeck
~~~~~~~~~~~~~~~~~~~~~

Main class responsable to make the API requests and call the validators.
"""


import requests

from . import validators


class YGOProDeck:
    url_cardinfo = 'https://db.ygoprodeck.com/api/v2/cardinfo.php'
    url_pics = 'https://ygoprodeck.com/pics/'

    session = requests.Session()

    def __init__(self, validate=True):
        self.validate = validate

    def make_request(self, url, **kwargs):
        """Make a HTTP request.

        Args:
            url (url): Api endpoint.

        Returns:
            (list[dict]): List of cards

        Raises:
            requests.exceptions.RequestException: Failed to connect
        """
        response = self.session.get(url, **kwargs)

        response.raise_for_status()

        return response.json()

    def get_all_cards(self):
        """Get all cards.

        Returns:
            (list[dict]): List of cards
        """
        return self.make_request(self.url_cardinfo)

    def get_cards(self, **params):
        """Get a list of cards.

        Args:
            name (str): The exact name of the card. You can also pass a card
                ID to this.
            fname (str): A fuzzy search using a string. For example &
                fname=Magician to search by all cards with "Magician" in the
                name.
            type_ (str): The type of card you want to filter by, type is a reserved word in python so use type_.
            atk (int): Filter by atk value.
            def_ (int): Filter by def value, def is a reserved word in python
                so use def_ to represente defense.
            level (int): Filter by card level/RANK.
            race (str): Filter by the card race which is officially called
                type (Spellcaster, Warrior, Insect, etc). This is also used
                for Spell/Trap cards.
            attribute (int): Filter by the card attribute.
            link (int): Filter the cards by Link value.
            linkmarker (str): Filter the cards by Link Marker value (Top,
                Bottom, Left, Right, Bottom-Left, Bottom-Right, Top-Left,
                Top-Right).
            scale (int): Filter the cards by Pendulum Scale value.
            set (str): Filter the cards by card set (Metal Raiders, Soul
                Fusion, etc).
            archetype (str): Filter the cards by archetype (Dark Magician,
                Prank-Kids, Blue-Eyes, etc).
            banlist (str): Filter the cards by banlist (TCG, OCG, Goat).
            sort (str): Sort the order of the cards (atk, def, name, type,
                level, id).
            la (str): Filter the cards by Language.

        Returns:
            (list[dict]): List of cards.
        """
        params = validators.remove_underline(params)

        if self.validate:
            params = self.validate_params(params)

        return self.make_request(self.url_cardinfo, params=params)

    def validate_params(self, params):
        """Validate query parameters before make HTTP request.

        Args:
            params (dict): Url query parameters.

        Returns:
            (dict): Validated url query parameters.

        Raises:
            YGOProDeckException: Parameter is not valid.
        """
        for key, value in params.items():
            if key in validators.validators.keys():
                if isinstance(value, str):
                    value = value.lower()

                validators.validators[key](value)

        return params
