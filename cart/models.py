from django.db import models
from product.models import VariationModel
from user.models import CustomUserModel


class CartModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItemMode(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    item = models.ForeignKey(VariationModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
