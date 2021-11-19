from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse


# Create your models here.


class ProductsCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    slug = AutoSlugField(populate_from='title')
    name = models.CharField(max_length=150, verbose_name='عنوان در URL')
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        related_name='children', on_delete=models.CASCADE
    )
    is_sub = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('eshop_products:products_list', args=[self.slug, ])


