# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0070_auto_20170919_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitanje5_4',
            name='Da_ne',
            field=models.CharField(choices=[('Da', 'Да'), ('Ne', 'Не')], max_length=100),
        ),
    ]
