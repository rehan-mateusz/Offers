import pytest

from offers import models
from offers.tests import factories

@pytest.fixture
def category():
    return factories.CategoryFactory()

@pytest.fixture
def category2():
    return factories.CategoryFactory(name='cat_2', ordering=2)
