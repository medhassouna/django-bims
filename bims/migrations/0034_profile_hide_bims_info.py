# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-16 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0033_merge_20180813_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hide_bims_info',
            field=models.BooleanField(default=False),
        ),
    ]