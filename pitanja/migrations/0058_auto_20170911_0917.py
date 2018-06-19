# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0057_saradnjaizmedjusubjekata_ko_su_korisnici_vasih_proizvoda_drugo'),
    ]

    operations = [
        migrations.AddField(
            model_name='saradnjaizmedjusubjekata',
            name='Kojem_modelu_finansiranja_NGIPA_treba_teziti_drugo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Којем моделу финансирања НИГП-а треба тежити друго'),
        ),
        migrations.AddField(
            model_name='saradnjaizmedjusubjekata',
            name='Model_odredjivanja_cene_drugo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Модел одређивања цене друго'),
        ),
    ]
