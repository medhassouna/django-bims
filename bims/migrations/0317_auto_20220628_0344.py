# Generated by Django 2.2.28 on 2022-06-28 03:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0316_auto_20220627_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biologicalcollectionrecord',
            name='record_type',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
