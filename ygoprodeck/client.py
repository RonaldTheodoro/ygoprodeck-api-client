#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ygoprodeck.Client
~~~~~~~~~~~~~~~~~~~~~

Main class responsable to make the API requests and call the validators.
"""


import requests

from . import validators


class Client(object):
    """Access the API and retrive the cards data"""

    url_base = 'https://db.ygoprodeck.com/api/v7'
    url_api = f'{url_base}/cardinfo.php'
    url_random_card = f'{url_base}/randomcard.php'
    url_card_sets = f'{url_base}/cardsets.php'
    url_card_sets_info = f'{url_base}/cardsetsinfo.php'
    url_archetypes = f'{url_base}/archetypes.php'
    url_db_version = f'{url_base}/checkDBVer.php'

    url_image_base = 'https://storage.googleapis.com/ygoprodeck.com'
    url_image = f'{url_image_base}/pics'
    url_image_small = f'{url_image_base}/pics_small'

    def __init__(self, validate=True, session=None):
        self.__card_data = None
        self.__validate = validate
        self.session = session

    @property
    def card_data(self):
        return self.__card_data

    @property
    def session(self):
        return self.__session

    @session.setter
    def session(self, session):
        self.__session = session or requests.Session()

    def __make_request(self, url=None, **kwargs):
        """Make a HTTP request.

        Args:
            url (url): Api endpoint.
            kwargs (dict): Requests params

        Returns:
            (list[dict]): List of cards

        Raises:
            requests.exceptions.RequestException: Failed to connect
        """
        if url is None:
            url = self.url_api

        response = self.__session.get(url, **kwargs)
        response.raise_for_status()
        return response.json()

    def get_all_cards(self):
        """Get all cards.

        Returns:
            (list[dict]): List of cards
        """
        if self.__card_data is None:
            self.__card_data = self.__make_request()
        return self.__card_data

    def get_random_card(self):
        """Get random card

        Returns:
            (dict): random card
        """
        return self.__make_request(url=self.url_random_card)

    def get_card_image(self, card_id):
        """Get card image

        Args:
            card_id (int): Card id

        Returns:
            (dict): random card
        """
        response = self.__session.get(f'{self.url_image}/{card_id}.jpg')
        response.raise_for_status()
        return response.content

    def get_card_image_small(self, card_id):
        """Get card image small

        Args:
            card_id (int): Card id

        Returns:
            (dict): random card
        """
        response = self.__session.get(f'{self.url_image_small}/{card_id}.jpg')
        response.raise_for_status()
        return response.content

    def get_card_sets(self):
        """Get all card sets

        Returns:
            (list[dict]): Card sets
        """
        return self.__make_request(url=self.url_card_sets)

    def get_card_sets_info(self, setcode):
        """Get all card sets info

        Args:
            setcode (str): Card setcode

        Returns:
            (list[dict]): Card sets info
        """
        params = {'setcode': setcode}
        return self.__make_request(url=self.url_card_sets_info, params=params)

    def get_archetypes(self):
        """Get all archtypes

        Returns:
            (list[dict]): Archtypes
        """
        return self.__make_request(url=self.url_archetypes)

    def get_api_database_version(self):
        """Get api database version

        Returns:
            (list[dict]): database version
        """
        return self.__make_request(url=self.url_db_version)

    def get_cards(self, **params):
        """Get a list of cards.

        Args:
            name (str): The exact name of the card. You can pass multiple |
                separated names to this parameter (Baby Dragon|Time Wizard).
            fname (str): A fuzzy search using a string. For example
                &fname=Magician to search by all cards with "Magician" in the
                name.
            id (str): The ID of the card. You cannot pass this alongside name.
                You can pass multiple comma separated IDs to this parameter.
            type_ (str): The type of card you want to filter by. See below
                "Card Types Returned" to see all available types. You can pass
                multiple comma separated Types to this parameter, def is a
                reserved word in python so use def_ to represente defense.
            atk (int): Filter by atk value.
            def_ (int): Filter by def value, def is a reserved word in python
                so use def_ to represente defense.
            level (int): Filter by card level/RANK.
            race (str): Filter by the card race which is officially called type
                (Spellcaster, Warrior, Insect, etc). This is also used for
                Spell/Trap cards. You can pass multiple comma separated Races
                to this parameter.
            attribute (int): Filter by the card attribute. You can pass
                multiple comma separated Attributes to this parameter.
            link (int): Filter the cards by Link value.
            linkmarker (str): Filter the cards by Link Marker value
                (Top, Bottom, Left, Right, Bottom-Left, Bottom-Right, Top-Left,
                Top-Right). You can pass multiple comma separated values to
                this parameter.
            cardset (str): Filter the cards by card set (Metal Raiders,
                Soul Fusion, etc).
            archetype (str): Filter the cards by archetype (Dark Magician,
                Prank-Kids, Blue-Eyes, etc).
            banlist (str): Filter the cards by banlist (TCG, OCG, Goat).
            sort (str): Sort the order of the cards (atk, def, name, type,
                level, id, new).
            format_ (str): Sort the format of the cards (tcg, goat, ocg goat,
                speed duel, rush duel, duel links). Note: Duel Links is not
                100% accurate but is close. Using tcg results in all cards with
                a set TCG Release Date and excludes Speed Duel/Rush Duel cards,
                format is a reserved word in python so use format_ to
                represente format.
            misc (str): Show additional response info (Card Views, Beta Name,
                etc.).
            staple (str): Check if card is a staple.
            has_effect (str): Check if a card actually has an effect or not by
                passing a boolean true/false. Examples of cards that do not
                have an actual effect: Black Skull Dragon, LANphorhynchus,
                etc etc.
            startdate (str): Query release dates for
                cards and the region of these release dates (TCG or OCG). What
                date format you pass to startdate and enddate can be slightly
                varied as our API picks up different formats and converts it
                regardless. For example: Jan 01 2000 or 01/01/2000
            nddate (str): Query release dates for
                cards and the region of these release dates (TCG or OCG). What
                date format you pass to startdate and enddate can be slightly
                varied as our API picks up different formats and converts it
                regardless. For example: Jan 01 2000 or 01/01/2000
            dateregion (str): Query release dates for
                cards and the region of these release dates (TCG or OCG). What
                date format you pass to startdate and enddate can be slightly
                varied as our API picks up different formats and converts it
                regardless. For example: Jan 01 2000 or 01/01/2000

        Returns:
            list[dict]: List of cards.
        """
        params = validators.remove_underline(params)

        if self.__validate:
            params = self.__validate_params(params)

        return self.__make_request(params=params)

    def __validate_params(self, params):
        """Validate query parameters before make HTTP request.

        Args:
            params (dict): Url query parameters.

        Returns:
            dict: Validated url query parameters.

        Raises:
            YGOProDeckException: Parameter is not valid.
        """

        validators.card_id_and_name(params)

        for key, value in params.items():
            if key in validators.validators.keys():
                if isinstance(value, str):
                    value = value.lower()

                validators.validators[key](value)

        return params
