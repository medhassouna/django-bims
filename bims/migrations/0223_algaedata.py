# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-04 03:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0222_auto_20200304_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlgaeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curation_process', models.CharField(blank=True, max_length=100, null=True)),
                ('indicator_chl_a', models.CharField(blank=True, default=b'', max_length=100, verbose_name=b'Biomass Indicator: Chl A')),
                ('chl_a', models.FloatField(blank=True, null=True, verbose_name=b'Chlorophyll a: benthic')),
                ('indicator_asdm', models.CharField(blank=True, default=b'', max_length=100, verbose_name=b'Biomass Indicator: Ash Free Dry Mass')),
                ('asdm', models.FloatField(blank=True, null=True, verbose_name=b'Ash Free Dry Mass')),
                ('ai', models.FloatField(blank=True, null=True, verbose_name=b'Autotrophic Index (AI)')),
                ('biological_collection_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='algae_data', to='bims.BiologicalCollectionRecord')),
            ],
        ),
    ]