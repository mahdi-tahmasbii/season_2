from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from eshop_products.models import *


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(ProductsList, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    count = models.IntegerField(verbose_name='تعداد')
    date = models.DateTimeField(auto_now_add=True)

    def get_detail_sum(self):
        return self.count * self.price

    def __str__(self):
        return self.product.title
