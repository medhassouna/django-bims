# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-04 15:48


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_curatedthumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
