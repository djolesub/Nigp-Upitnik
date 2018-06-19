# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0069_auto_20170919_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitanje3_2',
            name='Dostupnost',
            field=models.CharField(choices=[('интерно', 'интерно'), ('доступно свима', 'доступно свима')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='pitanje3_2',
            name='Prava_Pristupa',
            field=models.CharField(choices=[('интерно', 'интерно'), ('доступно свима', 'доступно свима')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='pitanje3_2',
            name='Web_Servis',
            field=models.CharField(choices=[('интерно', 'интерно'), ('доступно свима', 'доступно свима')], max_length=1000),
        ),
    ]