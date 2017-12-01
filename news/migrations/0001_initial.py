# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=30)),
                ('newslink', models.CharField(max_length=100)),
                ('Agency', models.CharField(max_length=30)),
            ],
        ),
    ]
