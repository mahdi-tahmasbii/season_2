# Generated by Django 3.2.9 on 2021-11-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0009_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
        migrations.AddField(
            model_name='productslist',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='eshop_products.IPAddress'),
        ),
    ]
