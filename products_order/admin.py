from django.contrib import admin

# Register your models here.
from .models import Order, OrderDetail


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order', 'product', 'price', 'count', 'date']
    list_editable = []

    class Meta:
        model = OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_paid', 'payment_date', 'date']
    list_editable = []

    class Meta:
        model = OrderDetail


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
