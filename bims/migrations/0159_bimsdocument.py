# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-22 05:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0028_auto_20170801_1228'),
        ('bims', '0158_biologicalcollectionrecord_source_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='BimsDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=512, null=True)),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='documents.Document')),
            ],
        ),
    ]
