# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0055_auto_20170911_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='saradnjaizmedjusubjekata',
            name='Na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni_drugo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='На који начин сарађујете са другим организацијама при размени података друго'),
        ),
    ]