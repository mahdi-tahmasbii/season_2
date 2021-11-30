import os

from django.db import models


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"logo-image/{final_name}"


# Create your models here.

class ContactInfo(models.Model):
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    about_us = models.TextField(null=True, blank=True)
    copy_right = models.CharField(null=True, blank=True, max_length=200)
    logo_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    is_read = models.BooleanField()

    def __str__(self):
        return self.subject


class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    about = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title


class CommonModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_image_path)
    link = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField()

    class Meta:
        abstract = True


class HomeSlider(CommonModel):
    def __str__(self):
        return self.title


class HomeSlider2(CommonModel):
    def __str__(self):
        return self.title


class Banner_1(CommonModel):
    def __str__(self):
        return self.title


class Banner_2(CommonModel):
    def __str__(self):
        return self.title


class Banner_3(CommonModel):
    def __str__(self):
        return self.title


class Banner_4(CommonModel):
    def __str__(self):
        return self.title


class Banner_5(CommonModel):
    def __str__(self):
        return self.title
