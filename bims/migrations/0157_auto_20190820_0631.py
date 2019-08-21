# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-20 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('td_biblio', '0003_auto_20181115_0808'),
        ('documents', '0033_auto_20180414_2120'),
        ('bims', '0156_auto_20190819_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SourceReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SourceReferenceBibliography',
            fields=[
                ('sourcereference_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bims.SourceReference')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='td_biblio.Entry')),
            ],
            options={
                'abstract': False,
            },
            bases=('bims.sourcereference',),
        ),
        migrations.CreateModel(
            name='SourceReferenceDatabase',
            fields=[
                ('sourcereference_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bims.SourceReference')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bims.DatabaseRecord')),
            ],
            options={
                'abstract': False,
            },
            bases=('bims.sourcereference',),
        ),
        migrations.CreateModel(
            name='SourceReferenceDocument',
            fields=[
                ('sourcereference_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bims.SourceReference')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Document')),
            ],
            options={
                'abstract': False,
            },
            bases=('bims.sourcereference',),
        ),
        migrations.AddField(
            model_name='sourcereference',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_bims.sourcereference_set+', to='contenttypes.ContentType'),
        ),
    ]