# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp


@pytest.fixture
def testapp(app):
    """Create Webtest app."""
    return TestApp(app)
