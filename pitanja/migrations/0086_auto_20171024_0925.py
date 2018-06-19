# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0085_auto_20171024_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitanje3_2',
            name='Dostupnost',
            field=models.CharField(choices=[('Интерно', 'Интерно'), ('Доступно свима', 'Доступно свима')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='pitanje3_2',
            name='Prava_Pristupa',
            field=models.CharField(choices=[('Интерно', 'Интерно'), ('Доступно свима', 'Доступно свима')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='pitanje3_2',
            name='Web_Servis',
            field=models.CharField(choices=[('Интерно', 'Интерно'), ('Доступно свима', 'Доступно свима')], max_length=1000),
        ),
    ]
