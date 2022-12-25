from rest_framework import serializers
from api.core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category object"""
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']
