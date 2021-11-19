from django.contrib import admin
from .models import ProductsList, Comment, ProductsGallery

# Register your models here.
admin.site.register(ProductsList)
admin.site.register(Comment)
admin.site.register(ProductsGallery)
