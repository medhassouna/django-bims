# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-01 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0217_update_default_fbis_site_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='chem',
            name='show_in_abiotic_list',
            field=models.BooleanField(default=False),
        ),
    ]