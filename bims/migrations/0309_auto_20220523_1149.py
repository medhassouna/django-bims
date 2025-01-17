# Generated by Django 2.2.28 on 2022-05-23 11:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0308_merge_20220523_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloadrequest',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='downloadrequest',
            name='resource_type',
            field=models.CharField(choices=[('CSV', 'Csv'), ('CHART', 'Chart'), ('TABLE', 'Table'), ('IMAGE', 'Image')], default='CSV', max_length=10),
        ),
    ]
