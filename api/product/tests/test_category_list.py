from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.core.models import Category

from api.product.serializers import CategorySerializer


CAT_URL = reverse('api.product:cat-list')
