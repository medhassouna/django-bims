# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-04 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0212_surveydata_surveydataoption_surveydatavalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveydata',
            name='display_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='surveydataoption',
            name='display_order',
            field=models.IntegerField(default=0),
        ),
    ]