# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0056_saradnjaizmedjusubjekata_na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni_drugo'),
    ]

    operations = [
        migrations.AddField(
            model_name='saradnjaizmedjusubjekata',
            name='Ko_su_korisnici_vasih_proizvoda_drugo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ко су корисници Ваших производа друго'),
        ),
    ]
