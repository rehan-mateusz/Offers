from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    category_id = serializers.SerializerMethodField('get_category_id')

    class Meta:
        model = models.Offer
        fields = ('id', 'title', 'description','price', 'category_id',
            'created_at')
        read_only = ('created_at',)

    def get_category_id(self, obj):
        return obj.category.id
