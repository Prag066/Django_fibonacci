# Generated by Django 2.2.4 on 2019-10-06 11:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fib', '0003_auto_20191006_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fib_data',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 6, 11, 38, 0, 591626, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fib_data',
            name='duretion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
