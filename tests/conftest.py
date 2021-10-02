#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import pytest
from betamax import Betamax

from .context import ygoprodeck
from .context import settings


with Betamax.configure() as config:
    config.cassette_library_dir = settings.cassettes_dir


@pytest.fixture
@pytest.mark.usefixtures('betamax_session')
def client_mock(betamax_session):
    return ygoprodeck.Client(validate=False, session=betamax_session)


@pytest.fixture
@pytest.mark.usefixtures('betamax_session')
def client(betamax_session):
    return ygoprodeck.Client(session=betamax_session)


@pytest.fixture
def card():
    return ygoprodeck.models.Card()


@pytest.fixture
def get_payload():

    def load_json(file_name):
        json_path = settings.test_payloads / file_name
        with json_path.open(mode='r') as fp:
            payload = json.load(fp)
        return payload

    return load_json
