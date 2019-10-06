# Generated by Django 2.2.4 on 2019-10-06 10:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fib_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('fib_list', models.TextField(blank=True, null=True)),
                ('duretion', models.DecimalField(blank=True, decimal_places=5, max_digits=5, null=True)),
                ('date', models.DateTimeField(verbose_name=datetime.datetime(2019, 10, 6, 10, 29, 6, 764405, tzinfo=utc))),
            ],
        ),
    ]
