# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0015_auto_20170726_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kadroviinfrastruktura',
            name='Serveri_za_prostorne_podatke',
            field=models.CharField(choices=[('ArcGIS Server (ESRI)', 'ArcGIS Server (ESRI)'), ('Autodesk Infrastructure Map Server', 'Autodesk Infrastructure Map Server'), ('GeoServer', 'GeoServer'), ('MapServer', 'MapServer'), ('ERDAS APOLLO', 'ERDAS APOLLO'), ('Ostalo', 'Ostalo')], max_length=100),
        ),
    ]