import pytest

from offers.tests import factories

from offers import models

@pytest.mark.django_db
def test_get_max_categories_amount(category):
    assert models.get_max_categories_amount() == 2

@pytest.mark.django_db
def test_get_max_categories_amount_without_any_category():
    assert models.get_max_categories_amount() == 1

@pytest.mark.django_db
def test_adjust_ordering_higher_to_lower(category, category2):
    models.adjust_ordering(1, category2.ordering)
    category.refresh_from_db()
    assert category.ordering == 2

@pytest.mark.django_db
def test_adjust_ordering_lower_to_higher(category, category2):
    models.adjust_ordering(2, category.ordering)
    category2.refresh_from_db()
    assert category.ordering == 1

@pytest.mark.django_db
def test_category_delete(category, category2):
    category.delete()
    category2.refresh_from_db()
    assert category2.ordering == 1
    assert not models.Category.objects.filter(id = category.id).exists()

@pytest.mark.django_db
def test_category_save_new_object():
    category = models.Category(name='test', ordering=1)
    category.save()
    assert models.Category.objects.filter(id = category.id).exists()

@pytest.mark.django_db
def test_category_save_edited_object(category):
    category.ordering = 2
    category.save()
    assert category.ordering==2
