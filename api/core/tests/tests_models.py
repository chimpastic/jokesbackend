from django.test import TestCase
from django.contrib.auth import get_user_model
from api.core import models


def sample_user(email='test@mugdh.com,', password='Password@123'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Test creating a new user with an email is successful"""
        email = 'test@mugdh.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_category_str(self):
        """Test the models that returns the category string """
        category = models.Category.create(
            user=sample_user(),
            name='MDF'
        )
        self.assertEqual(str(category), category.name)
