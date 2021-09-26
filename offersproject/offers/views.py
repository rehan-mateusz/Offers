from rest_framework import viewsets

from . import models
from . import serializers


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OfferSerializer
    queryset = models.Offer.objects.all()


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all().order_by('ordering')
