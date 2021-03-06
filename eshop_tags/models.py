from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    name = models.CharField(max_length=150, verbose_name='عنوان در URL')
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    is_color = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

    def get_absolute_url(self):
        return reverse('eshop_products:products_list', args=[self.slug, ])
