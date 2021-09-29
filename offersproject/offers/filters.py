from django_filters import rest_framework as filters

from . import models

class OfferFilter(filters.FilterSet):
    category = filters.CharFilter(
        lookup_expr='iexact',
        label='category',
        field_name='category__id')
    class Meta:
        model = models.Offer
        fields = {}
