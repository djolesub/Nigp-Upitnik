# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-26 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0088_auto_20171225_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitanje3_3',
            name='Proizvod',
            field=models.CharField(choices=[('*****************************', '*****************************'), ('Катастарске парцеле и објекти', 'Катастарске парцеле и објекти'), ('Подаци катастра непокретности', 'Подаци катастра непокретности'), ('Ортофото', 'Ортофото'), ('Адресе', 'Адресе'), ('Топографске карте', 'Топографске карте (1:20 000 и ситније размере)'), ('Основна државна карта', 'Основна државна карта (1:5000; 1:10 000)'), ('Просторни планови', 'Просторни планови'), ('Остало', 'Остало')], max_length=100),
        ),
        migrations.AlterField(
            model_name='pitanje3_3',
            name='Proizvodjac',
            field=models.CharField(choices=[('Не користимо ову врсту апликације', 'Не користимо ову врсту апликације'), ('РГЗ', 'Републички геодетски завод'), ('ВГИ', 'Војногеографски институт'), ('Завод за заштиту природе Србије', 'Завод за заштиту природе Србије'), ('Републички завод за статистику', 'Републички завод за статистику'), ('Републичка дирекција за воде', 'Републичка дирекција за воде'), ('Републички хидрометролошки завод', 'Републички хидрометролошки завод'), ('Завод за заштиту споменика културе', 'Завод за заштиту споменика културе'), ('ЈП Пошта Србије', 'ЈП Пошта Србије'), ('ЈП Путеви Србије', 'ЈП Путеви Србије'), ('European Environment Agency', 'European Environment Agency (EEA)'), ('Остало', 'Остало')], max_length=100),
        ),
        migrations.AlterField(
            model_name='pitanje3_3',
            name='Prostorni_Obuhvat',
            field=models.CharField(choices=[('***************************', '***************************'), ('Територија Републике Србије', 'Територија Републике Србије'), ('Територија административне надлежности организације', 'Територија административне надлежности организације'), ('Остало', 'Остало')], max_length=100),
        ),
        migrations.AlterField(
            model_name='standardizacijaotvorenihpodataka',
            name='Koju_vrstu_podataka_ste_koristili',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Просторни подаци', 'Просторни подаци'), ('Финансијски подаци', 'Финансијски подаци'), ('Статистички подаци', 'Статистички подаци'), ('Научни подаци', 'Научни подаци'), ('Подаци о времену', 'Подаци о времену'), ('Подаци о култури', 'Подаци о култури'), ('Подаци о животној средини', 'Подаци о животној средини'), ('Подаци јавног сектора', 'Подаци јавног сектора'), ('Друго', 'Друго')], max_length=1000),
        ),
    ]
