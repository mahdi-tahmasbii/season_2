# Generated by Django 3.2.9 on 2021-11-20 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop_products', '0005_auto_20211119_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productslist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
