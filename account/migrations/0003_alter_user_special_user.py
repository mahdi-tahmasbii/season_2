# Generated by Django 3.2.9 on 2021-11-19 18:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211119_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 19, 18, 45, 50, 832018, tzinfo=utc), verbose_name='کاربر ویژه تا'),
        ),
    ]
