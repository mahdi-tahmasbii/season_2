# Generated by Django 3.2.9 on 2021-11-29 11:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_alter_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 11, 37, 25, 95790, tzinfo=utc), verbose_name='کاربر ویژه تا'),
        ),
    ]