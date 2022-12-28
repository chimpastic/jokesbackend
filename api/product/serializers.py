from rest_framework import serializers
from api.core.models import Category
from api.core.models import Product


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category object"""
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'category_id', 'name', 'description', 'product_image')
        read_only_fields = ('id',)
