from django.db import models
from user.models import CustomUserModel
from cart.models import CartModel


class OrderModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255, default='')
    order_description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)
