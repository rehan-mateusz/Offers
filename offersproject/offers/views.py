from rest_framework import viewsets
from rest_framework.response import Response

from . import models
from . import serializers
from . import filters


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OfferSerializer
    queryset = models.Offer.objects.all()
    filterset_class = filters.OfferFilter
    

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all().order_by('ordering')
