# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0077_auto_20171023_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saradnjaizmedjusubjekata',
            name='Da_li_Podrzavate_razmenu_podataka_preko_portala_e_placanje',
            field=models.CharField(blank=True, choices=[('Да', 'Да, подржавамо'), ('Не', 'Не, не подржавамо')], max_length=100, null=True),
        ),
    ]
