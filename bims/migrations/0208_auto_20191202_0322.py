# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-02 03:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bims', '0207_auto_20191124_0534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name=b'sites',
        ),
        migrations.AddField(
            model_name='survey',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='survey',
            name='ready_for_validation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='bims.LocationSite'),
        ),
        migrations.AddField(
            model_name='survey',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='validation_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
