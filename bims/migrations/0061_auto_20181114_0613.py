# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-14 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('td_biblio', '0001_initial'),
        ('bims', '0060_auto_20181105_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='biologicalcollectionrecord',
            name='institution_id',
            field=models.CharField(default=b'bims', help_text=b'An identifier for the institution having custody of the object(s) or information referred to in the record.', max_length=100, verbose_name=b'Custodian'),
        ),
        migrations.AlterField(
            model_name='locationsite',
            name='latitude',
            field=models.FloatField(blank=True, help_text=b'This is intended only for IPT', null=True),
        ),
        migrations.AlterField(
            model_name='locationsite',
            name='longitude',
            field=models.FloatField(blank=True, help_text=b'This is intended only for IPT', null=True),
        ),
        migrations.AddField(
            model_name='referencelink',
            name='collection_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bims.BiologicalCollectionRecord'),
        ),
        migrations.AddField(
            model_name='referencelink',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='td_biblio.Entry'),
        ),
    ]