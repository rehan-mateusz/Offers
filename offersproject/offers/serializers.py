from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Offer
        fields = '__all__'

class OfferListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Offer
        fields = ('id', 'title', 'price', 'category')
