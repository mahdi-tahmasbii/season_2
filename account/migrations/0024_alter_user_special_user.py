# Generated by Django 3.2.9 on 2021-11-30 11:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_alter_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 30, 11, 41, 25, 875418, tzinfo=utc), verbose_name='کاربر ویژه تا'),
        ),
    ]