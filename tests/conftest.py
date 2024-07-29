# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Mojib Wali.
# Copyright (C) 2020-2024 Graz University of Technology.
#
# invenio-config-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""


import pytest
from flask import Flask
from flask_principal import Identity, UserNeed
from invenio_access.permissions import any_user, authenticated_user

from invenio_config_tugraz import InvenioConfigTugraz


@pytest.fixture(scope="module")
def create_app(instance_path: str) -> Flask:
    """Application factory fixture."""

    def factory(**config: str) -> Flask:
        app = Flask("testapp", instance_path=instance_path)
        app.config.update(**config)
        InvenioConfigTugraz(app)
        return app

    return factory


@pytest.fixture(scope="function")
def anyuser_identity():
    """System identity."""
    identity = Identity(1)
    identity.provides.add(any_user)
    return identity


@pytest.fixture(scope="function")
def authenticated_identity():
    """Authenticated identity fixture."""
    identity = Identity(100)
    identity.provides.add(UserNeed(100))
    identity.provides.add(authenticated_user)
    return identity
