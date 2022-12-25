from rest_framework import viewsets, mixins
from api.core.models import Category
from api.product import serializers


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage the category in database"""

    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
