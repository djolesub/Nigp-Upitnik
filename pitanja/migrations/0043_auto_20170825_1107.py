# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-25 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0042_auto_20170825_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitanje5_4',
            name='Da_ne',
            field=models.CharField(blank=True, choices=[('Da', 'Ne'), ('Да', 'Не')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='saradnjaizmedjusubjekata',
            name='Da_li_Podrzavate_razmenu_podataka_preko_portala_e_placanje',
            field=models.CharField(blank=True, choices=[('Da', 'Ne'), ('Да, подржавамо', 'Не, не подржавамо')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='standardizacijaotvorenihpodataka',
            name='Ostalo',
            field=models.TextField(blank=True, help_text='Ваше мишљење о стању у геосектору, сарадњи између организација које производе и/или користе\t\t\t\t\t\t\t\t\t  просторне податке, расподели надлежности над сетовима података, ценовној политици и сл.', null=True, verbose_name='44. Простор за додатни коментар на питања која нису обухваћена овим упитником'),
        ),
    ]