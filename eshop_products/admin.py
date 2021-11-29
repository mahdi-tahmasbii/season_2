from django.contrib import admin
from .models import ProductsList, ProductsGallery, IPAddress

# Register your models here.
admin.site.register(ProductsList)
# admin.site.register(Comment)
admin.site.register(ProductsGallery)
admin.site.register(IPAddress)
