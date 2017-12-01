# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20171130_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Agency',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 30, 12, 35, 55, 997198)),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
