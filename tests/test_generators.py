# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Mojib Wali.
#
# invenio-config-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

from elasticsearch_dsl.query import Q

from invenio_config_tugraz.generators import AnyUserIfPublic, RecordIp


def test_recordip():
    generator = RecordIp()

    assert generator.needs() == []
    assert generator.excludes() == []
    assert generator.query_filter() == []


def test_AnyUserIfPublic():
    generator = AnyUserIfPublic()

    assert generator.needs() == []
    assert generator.excludes() == []
    assert generator.query_filter() == Q("match", **{"access.access_right": "open"})
