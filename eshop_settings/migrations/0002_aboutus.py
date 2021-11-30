# Generated by Django 3.2.9 on 2021-11-30 11:41

from django.db import migrations, models
import eshop_settings.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('about', models.EmailField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.upload_image_path)),
            ],
        ),
    ]
