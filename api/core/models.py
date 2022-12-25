import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


def product_image_file_path(instance, filename):
    ext = filename.split('.',)[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('product/', filename)


class Category(models.Model):
    """Category model for Product cateory"""

    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product Model for storing the products object"""

    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    product_image = models.ImageField(upload_to=product_image_file_path)

    def __str__(self):
        return self.name
