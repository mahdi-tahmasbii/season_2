# Generated by Django 3.2.9 on 2021-12-01 09:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_alter_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 1, 9, 4, 45, 807011, tzinfo=utc), verbose_name='کاربر ویژه تا'),
        ),
    ]