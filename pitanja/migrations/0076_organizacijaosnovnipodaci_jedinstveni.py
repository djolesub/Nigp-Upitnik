# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0075_auto_20170922_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizacijaosnovnipodaci',
            name='Jedinstveni',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
