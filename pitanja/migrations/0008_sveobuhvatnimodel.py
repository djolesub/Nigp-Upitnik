# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0007_pitanje5_1_pitanje5_12_pitanje5_13_pitanje5_14_pitanje5_2_pitanje5_4_standardizacijaotvorenihpodatak'),
    ]

    operations = [
        migrations.CreateModel(
            name='SveobuhvatniModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cetvrta_sekcija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.SaradnjaIzmedjuSubjekata')),
                ('Druga_sekcija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.KadroviInfrastruktura')),
                ('Peta_sekcija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.StandardizacijaOtvorenihPodataka')),
                ('Prva_sekcija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.OrganizacijaOsnovniPodaci')),
                ('Treca_sekcija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.ProstorniPodaci')),
            ],
        ),
    ]
