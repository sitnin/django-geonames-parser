# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_names', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryAlternate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('iso_language', models.CharField(max_length=3)),
                ('geoname_id', models.PositiveIntegerField()),
                ('datetime_create', models.DateTimeField(auto_now_add=True)),
                ('datetime_update', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(to='geo_names.Country')),
            ],
        ),
    ]
