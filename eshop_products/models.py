import os.path
from django.urls import reverse
from account.models import User
from django.db import models
from django.db.models import Q
from autoslug import AutoSlugField

import eshop_categories.models
from eshop_categories.models import ProductsCategory
from eshop_tags.models import Tag


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


class ProductsManager(models.Manager):
    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_tag(self, tag_name):
        return self.get_queryset().filter(tag_name_iexact=tag_name, active=True)

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class ProductsList(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),  # draft
        ('p', "منتشر شده"),  # publish
        ('i', "در حال بررسی"),  # investigation
        ('b', "برگشت داده شده"),  # back
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()
    full_info_description = models.TextField(null=True, blank=True, default=0)
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True, )
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    categories = models.ManyToManyField(ProductsCategory, related_name='products', blank=True)
    tag = models.ManyToManyField(Tag, blank=True, related_name='products')
    visit_count = models.IntegerField(default=0)
    Weight = models.CharField(max_length=200, default='')
    Materials = models.CharField(max_length=200, default='')
    Dimensions = models.CharField(max_length=200, default='')
    Other_Info = models.CharField(max_length=200, default='')
    is_especial = models.BooleanField(default=False, null=True, blank=True)
    offer = models.BooleanField(default=False, null=True, blank=True)
    our_suggestion = models.BooleanField(default=False, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    objects = ProductsManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"


class ProductsGallery(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),  # draft
        ('p', "منتشر شده"),  # publish
        ('i', "در حال بررسی"),  # investigation
        ('b', "برگشت داده شده"),  # back
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name='تصویر')
    product = models.ForeignKey(ProductsList, on_delete=models.CASCADE, verbose_name='محصول')

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(ProductsList, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    message = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return f'{self.name}'
