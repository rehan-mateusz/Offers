from factory.django import DjangoModelFactory

from offers import models


class CategoryFactory(DjangoModelFactory):

    class Meta:
        model = models.Category

    name = 'test_cat'
    ordering = 1

class OfferFactory(DjangoModelFactory):

    class Meta:
        model = models.Offer

    title = 'test_title'
    description = 'desc'
    price = 30
    category = None
