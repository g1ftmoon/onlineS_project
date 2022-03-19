from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from applications.project.models import Product

User = get_user_model()


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='review')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])

    def get_absolute_url(self):
        return f'/product-detail/{self.product.id}'

    def __str__(self):
        return self.title
