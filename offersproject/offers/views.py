from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

from . import models
from . import serializers
from . import filters


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OfferSerializer
    queryset = models.Offer.objects.all()
    filterset_class = filters.OfferFilter

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.OfferListSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all().order_by('ordering')
