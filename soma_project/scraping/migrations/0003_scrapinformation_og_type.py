# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-28 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_auto_20160828_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapinformation',
            name='og_type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
