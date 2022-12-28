from rest_framework import viewsets, mixins
from api.core.models import Category, Product
from api.product import serializers


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage the category in database"""

    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Manage receipe in the database"""
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
