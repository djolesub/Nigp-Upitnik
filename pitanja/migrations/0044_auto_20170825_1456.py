# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-25 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0043_auto_20170825_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitanje5_4',
            name='Da_ne',
            field=models.CharField(blank=True, choices=[('Da', 'Да'), ('Ne', 'Не')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prostornipodaci',
            name='Dodatno_obrazovanje_u_okviru_organizacije',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Стандардизација геопроизвода и сервиса', 'Стандардизација геопроизвода и сервиса'), ('Дефинисање техничке спецификације за геоподатке', 'Дефинисање техничке спецификације за геоподатке'), ('Метаподаци', 'Метаподаци (креирање, стандардизације, израда каталога и сервиса)'), ('Израда web сервиса за геоподатке', 'Израда web сервиса за геоподатке'), ('Развој техничке инфраструктуре', 'Развој техничке инфраструктуре'), ('Креирања тематских речника', 'Креирања тематских речника'), ('Дефинисање политике размене, приступа и безбедности података', 'Дефинисање политике размене, приступа и безбедности података'), ('Друго', 'Друго')], max_length=255),
        ),
        migrations.AlterField(
            model_name='prostornipodaci',
            name='Nacin_razmene_podataka_sa_drugima',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Директно преузимање', 'Директно преузимање (дигитални медиј, папир)'), ('Преузимање преко интернета', 'Преузимање преко интернета (download: HTTP и FTP )'), ('Web сервиси', 'Web сервиси')], max_length=58),
        ),
        migrations.AlterField(
            model_name='saradnjaizmedjusubjekata',
            name='Da_li_Podrzavate_razmenu_podataka_preko_portala_e_placanje',
            field=models.CharField(blank=True, choices=[('Da', 'Да, подржавамо'), ('Не', 'Не, не подржавамо')], max_length=100, null=True),
        ),
    ]
