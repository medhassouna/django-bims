# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-08 06:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0187_auto_20191008_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='biologicalcollectionrecord',
            name='abundance_type',
            field=models.CharField(blank=True, choices=[(b'number', b'Number'), (b'percentage', b'Percentage'), (b'density', b'Density')], default=b'number', max_length=50),
        ),
        migrations.AddField(
            model_name='biologicalcollectionrecord',
            name='specific_biotope',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specific_biotope', to='bims.Biotope'),
        ),
        migrations.AddField(
            model_name='biologicalcollectionrecord',
            name='substratum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biotope_substratum', to='bims.Biotope'),
        ),
    ]
