# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0019_auto_20170731_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kadroviinfrastruktura',
            name='Koje_aplikacije_su_u_upotrebi_za_obradu',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pitanja.Pitanje2_5'),
        ),
        migrations.AlterField(
            model_name='kadroviinfrastruktura',
            name='Koji_sistemi_za_upravljanje_bazama_imate',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pitanja.Pitanje2_6'),
        ),
        migrations.AlterField(
            model_name='kadroviinfrastruktura',
            name='Mobilne_gis_aplikacije',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pitanja.Pitanje2_8'),
        ),
    ]
