from django.contrib import admin
from .models import ProductsList, ProductsGallery

# Register your models here.
admin.site.register(ProductsList)
# admin.site.register(Comment)
admin.site.register(ProductsGallery)
