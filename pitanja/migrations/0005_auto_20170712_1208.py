# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0004_auto_20170712_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aneks1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aneks1_polje', models.CharField(choices=[('Координатни референтни системи', 'Координатни референтни системи(Системи за јединствено одређивање просторних информација у простору као скупа координата (x, y, z) и/или географске ширине и географске дужине и висине, на основу геодетског хоризонталног и вертикалног датума.)'), ('Коришћење земљишта', 'Коришћење земљишта(Територија описана у складу с постојећом и будућом планираном функционалном димензијом или друштвено-економском намена (нпр. стамбена, индустријска. комерцијална, пољопривредна, шумска, рекреативна).)'), ('Географски мрежни системи', 'Географски мрежни системи(Хармонизована мрежа вишеструке резолуције са заједничком почетном тачком и стандардизованом локацијом и величином мрежних ћелија.)'), ('Здравље људи и безбедност', 'Здравље људи и безбедност(Информације о географској дистрибуцији доминантних патологија (алергије, канцери, болести дисајних органа итд.), које указују на утицај на здравље (биомаркери, смањење плодности, епидемије) или добробит људи (замор, стрес итд.) у директној (загађивање ваздуха, хемикалије, смањење озонског омотача, бука итд.) или индиректној вези (храна, генетски модификовани организми итд.) с квалитетом животне средине.)'), ('Географска имена', 'Географска имена(Имена подручја, региона, локалитета, градова, предграђа, градова или насеља, или било који географски или топографски објекат од јавног или историјског интереса.)'), ('Водови и јавни сервиси', 'Водови и јавни сервиси(Подразумева водове као што су канализација, управљање отпадом, снабдевање енергијом и водом, административне и државне социјалне службе као што су државна администрација, локације цивилне заштите, школе и болнице.)'), ('Административне јединице', 'Административне јединице(Административне јединице, које раздвајају подручја на којима државе чланице имају и/или остварују права у вези са надлежношћу, за локалну, регионалну и националну управу, и која су одвојена административним границама.)'), ('Системи за праћење квалитета животне средине', 'Системи за праћење квалитета животне средине(Локација и функцијасистема за праћење животне средине укључујући посматрање и мерење емисије загађујућих материја, стања животне средине и других параметара екосистема (биодиверзитета, еколошких услова вегетације итд.) од стране или у име органа јавне власти.)'), ('Адресе', 'Адресе(Локација непокретности на основу адресних идентификатора, обично имена улице, кућног броја, поштанског броја.)'), ('Производни и индустријски системи', 'Производни и индустријски системи(Локације индустријске производње, укључујући инсталације за спречавање и контролу загађења, црпна постројења за воду, руднике, складишта и сл.)'), ('Катастарске парцеле', 'Катастарске парцеле(Подручја одређена катастарским регистрима или њиховим еквивалентима.)'), ('Системи за пољопривреду и аквакултуру', 'Системи за пољопривреду и аквакултуру(Пољопривредна опрема и објекти за производњу (укључујући системе за наводњавање, стакленици и штале).)'), ('Транспортне мреже', 'Транспортне мреже(Друмске, железничке, ваздушне и водне транспортне мреже и припадајућа '), ('Распрострањеност становништва – демографија', 'Распрострањеност становништва – демографија(Географска распрострањеност људи, укључујући '), ('Хидрографија', 'Хидрографија(Хидрографски елементи, укључујући морска подручја и сва друга водена тела и припадајуће делове, укључујући речне сливове и подсливове.)'), ('Област управљања', 'Област управљања/ограничења/зоне регулисања и јединице за извештавање (депоније, ограничена подручја око извора воде, зоне ограничења буке)(Области којима се управља, које се регулишу или користе за извештавање на међународном, европском, националном, регионалном и локалном нивоу. Укључује депоније, рестриктивне зоне око изворишта пијаће воде, зоне осетљиве на нитрате, уређене пловне путеве на мору или великим унутрашњим водама, области за одлагање отпада, зоне где се ограничава ниво буке, области за које је потребна дозвола за истраживање или рударство, области речних сливова, релевантне јединице извештавања и област управљања обалском зоном.)'), ('Заштићена подручја', 'Заштићена подручја(Област која је одређена или којом се управља у оквиру међународног законодавства, законодавства Заједнице и држава чланица, са циљем постизања посебних циљева очувања.)'), ('Зоне природног ризика', 'Зоне природног ризика(Осетљива подручја која се описују према природним хазардима (све атмосферске, хидролошке, сеизмичке, вулканске појаве и пожари, а који, због своје локације, озбиљности и учесталости имају потенцијал да озбиљно угрозе друштво), нпр. поплаве, одрони и улегнућа, лавине, шумски пожари, земљотреси, вулканске ерупције.)')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Aneks2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aneks2_polje', models.CharField(choices=[('Атмосферски услови', 'Атмосферски услови(Укључују просторне податке засноване на мерењима, моделима или њиховој комбинацији и укључују локације за мерење.)'), ('Висине', 'Висине(Дигитални  модели висина за површину копна, леда и океана. Укључује висину терена, батиметрију и линију обале.)'), ('Метеоролошко-географске карактеристике', 'Метеоролошко-географске карактеристике(Временски услови и њихове мерења; падавине, температура, испаравање, брзина и смер ветра.)'), ('Земљишни покривач', 'Земљишни покривач(Физичка и биолошка покривеност земљине површине укључујући вештачке површине, пољопривредне области, шуме, (полу)природне области, влажна земљишта, водна тела.)'), ('Биогеографски региони', 'Биогеографски региони(Области релативно хомогених еколошких услова са заједничким карактеристикама.)'), ('Ортофото', 'Ортофото(Геореференцирани снимци Земљине површине, прикупљени сателитским или аеро сензорима.)'), ('Станишта и биотопи', 'Станишта и биотопи(Географске области које карактеришу специфични еколошки услови, процеси, структура и функције (за одржавање живота) које физички омогућавају организмима да ту живе. Укључује копнене и водене површине које се разликују својим географским, абиотским и биотским карактеристикама, потпуно природним или полуприродним.)'), ('Геологија', 'Геологија(Геологија описана према саставу и структури. Укључује стеновито тло, водоносне слојеве и геоморфологију.)')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Aneks3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aneks3_polje', models.CharField(choices=[('Распрострањеност врста', 'Распрострањеност врста(Географска распрострањеност животињских и биљних врста, разврстаних по мрежи, региону, административној јединици или другој аналитичкој јединици.)'), ('Статистичке јединице', 'Статистичке јединице(Јединице за дистрибуцију или коришћење статистичких података.)'), ('Енергетски ресурси', 'Енергетски ресурси(Енергетски ресурси укључујући угљоводонике, енергију воде, биоенергију, соларну енергију, енергију ветра итд. а по потреби и информације о дубини/висини које се односе на величину ресурса.)'), ('Зграде', 'Зграде(Географска локација зграда.)'), ('Минерални ресурси', 'Минерални ресурси(Минерални ресурси укључују руде метала, индустријске минерале итд. а по потреби и информације о дубини/висини  које се односе на величину ресурса.)'), ('Тло', 'Тло(Тло и слојеви тла испод површине описани према дубини, текстури, структури и садржају честица и органског материјала, каменитости, ерозији, а по потреби просечног нагиба и предвиђени капацитет за чување воде.)')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pitanje3_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aneks1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.Aneks1')),
                ('Aneks2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.Aneks2')),
                ('Aneks3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.Aneks3')),
            ],
        ),
        migrations.CreateModel(
            name='Pitanje3_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Naziv_Proizvoda', models.CharField(max_length=100)),
                ('Opis_Proizvoda', models.CharField(max_length=100)),
                ('Digitalni_Format', models.BooleanField(max_length=100)),
                ('Nacin_skladistenja', models.CharField(choices=[('gdb', 'ESRI file geodatabase (*.gdb)'), ('mdb', 'ESRI personal geodatabase (*.mdb)'), ('MS Access', 'MS Access'), ('Oracle ', 'Oracle '), ('PostgreSQL', 'PostgreSQL'), ('MicrosoftSQL', 'MicrosoftSQL'), ('Фолдерска структура на серверима', 'Фолдерска структура на серверима'), ('Остало', 'Остало')], max_length=100)),
                ('Format_Distribucije', models.CharField(choices=[('Adobe PDF', 'Adobe PDF (*.pdf)'), ('ASCII gridded', 'ASCII gridded data format (*.xyz)'), ('GeoTIFF', 'GeoTIFF (*.tif)'), ('TIFF', 'TIFF (*.tif)'), ('CorelDraw', 'CorelDraw file format (*.cdr)'), ('TIFF', 'TIFF (*.tif), TFW (*.tfw)'), ('ECW', 'ECW Image file format (*.ecw)'), ('MrSID', 'MrSID file format (*.sid)'), ('ESRI', 'ESRI shapefile (*.shp)'), ('MapInfo ', 'MapInfo TAB format (*.tab)'), ('KML', 'KML file format (*.kml, *.kmz)'), ('IMG ', 'IMG file format (*.img)'), ('NTF', 'NTF Image file format (*.ntf)'), ('AutoCAD DXF', 'AutoCAD DXF (*.dxf)'), ('ESRI file', 'ESRI file geodatabase (*.gdb)'), ('ESRI personal', 'ESRI personal geodatabase (*.mdb)'), ('JPG', 'JPG file format (*.jpg)'), ('Microsoft Excel', 'Microsoft Excel file format (*.xls)'), ('Остало', 'Остало')], max_length=100)),
                ('Nacin_Distribucije', models.CharField(choices=[('Поштом', 'Поштом'), ('Преко имејла', 'Преко имејла'), ('Директно преузимање ', 'Директно преузимање (дигитални медиј, папир)'), ('Преузимање преко интернета', 'Преузимање преко интернета (download: HTTP и FTP )'), ('Web сервиси', 'Web сервиси'), ('Ostalo', 'Ostalo')], max_length=100)),
                ('Tacnost', models.CharField(max_length=100)),
                ('Koordinatni_Sistem', models.CharField(choices=[('Гаус-Кригер', 'Гаус-Кригер'), ('ETRS89/UTM', 'ETRS89/UTM'), ('Географски координатни систем', 'Географски координатни систем'), ('Подаци нису просторно одређени', 'Подаци нису просторно одређени - геореференцирани'), ('Ostalo', 'Ostalo')], max_length=100)),
                ('Obuhvaceno_Podrucje', models.CharField(max_length=100)),
                ('Period_Azuriranja', models.CharField(choices=[('У континуитету', 'У континуитету'), ('По потреби', 'По потреби'), ('Периодично', 'Периодично – на сваких XXX дана'), ('Према прописима', 'Према прописима'), ('Преиспитивање плана', 'Преиспитивање плана'), ('Остало', 'Остало')], max_length=100)),
                ('Metapodaci', models.BooleanField()),
                ('Dostupnost', models.CharField(choices=[('интерно', 'интерно'), ('доступно свима', 'доступно свима')], max_length=100)),
                ('Web_Servis', models.CharField(choices=[('интерно', 'интерно'), ('доступно свима', 'доступно свима')], max_length=100)),
                ('Prava_Pristupa', models.CharField(choices=[('интерно', 'интерно'), ('доступно свима', 'доступно свима')], max_length=100)),
                ('Naknada', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pitanje3_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Proizvod', models.CharField(choices=[('Катастарске парцеле и објекти', 'Катастарске парцеле и објекти'), ('Подаци катастра непокретности', 'Подаци катастра непокретности'), ('Ортофото', 'Ортофото'), ('Адресе', 'Адресе'), ('Топографске карте', 'Топографске карте (1:20 000 и ситније размере)'), ('Основна државна карта', 'Основна државна карта (1:5000; 1:10 000)'), ('Просторни планови', 'Просторни планови'), ('Друго', 'Друго')], max_length=100)),
                ('Proizvodjac', models.CharField(choices=[('РГЗ', 'Републички геодетски завод'), ('ВГИ', 'Војногеографски институт'), ('Завод за заштиту природе Србије', 'Завод за заштиту природе Србије'), ('Републички завод за статистику', 'Републички завод за статистику'), ('Републичка дирекција за воде', 'Републичка дирекција за воде'), ('Републички хидрометролошки завод', 'Републички хидрометролошки завод'), ('Завод за заштиту споменика културе', 'Завод за заштиту споменика културе'), ('ЈП Пошта Србије', 'ЈП Пошта Србије'), ('ЈП Путеви Србије', 'ЈП Путеви Србије'), ('European Environment Agency', 'European Environment Agency (EEA)'), ('Друго', 'Друго')], max_length=100)),
                ('Prostorni_Obuhvat', models.CharField(choices=[('Територија Републике Србије', 'Територија Републике Србије'), ('Територија административне надлежности организације', 'Територија административне надлежности организације'), ('Друго', 'Друго')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pitanje3_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Koordinatni_referentni_sistemi', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Geografski_mrezni_sistemi', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Geografska_imena', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Administrativne_jedinice', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Adrese', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Katastarske_parcele', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Transportne_mreze', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Hidrografija', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Zasticena_podrucja', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Visine', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Zemljisni_pokrivac', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Ortofoto', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Geologija', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Statisticke_jedinice', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Zgrade', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Tlo', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Koriscenje_zemljista', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Zdravlje_ljudi_I_bezbednost', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Vodovi_i_javni_servisi', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Sistemi_za_pracenje_kvaliteta_zivotne_sredine', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Proizvodni_i_industrijski_sistemi', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Sistemi_za_poljoprivredu_i_akvakulturu', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Rasprostranjenost_stanovnistva_demografija', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Oblast_upravljanja', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Zone_prirodnog_rizika', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Atmosferski_uslovi', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Meteorolosko_geografske_karakteristike', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Biogeografski_Regioni', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Stanista_i_biotopi', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Rasprostranjenost_vrsta', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Energetski_resursi', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
                ('Mineralni_resursi', models.CharField(choices=[('Није од значаја', 'Није од значаја'), ('Делимично значајно', 'Делимично значајно'), ('Значајно', 'Значајно'), ('Од великог значаја', 'Од великог значаја'), ('Изузетно значајно', 'Изузетно значајно')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pitanje3_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Proizvod', models.CharField(choices=[('Катастарске парцеле и објекти', 'Катастарске парцеле и објекти'), ('Подаци катастра непокретности', 'Подаци катастра непокретности'), ('Ортофото', 'Ортофото'), ('Адресе', 'Адресе'), ('Топографске карте ', 'Топографске карте (1:20 000 и ситније размере)'), ('Основна државна карта', 'Основна државна карта (1:5000; 1:10 000)'), ('Просторни планови', 'Просторни планови'), ('Друго', 'Друго')], max_length=100)),
                ('Proizvodjac', models.CharField(choices=[('РГЗ', 'Републички геодетски завод'), ('ВГИ', 'Војногеографски институт'), ('Завод за заштиту природе Србије', 'Завод за заштиту природе Србије'), ('Републички завод за статистику', 'Републички завод за статистику'), ('Републичка дирекција за воде', 'Републичка дирекција за воде'), ('Републички хидрометролошки завод', 'Републички хидрометролошки завод'), ('Завод за заштиту споменика културе', 'Завод за заштиту споменика културе'), ('ЈП Пошта Србије', 'ЈП Пошта Србије'), ('ЈП Путеви Србије', 'ЈП Путеви Србије'), ('European Environment Agency', 'European Environment Agency (EEA)'), ('Друго', 'Друго')], max_length=100)),
                ('Prostorni_obuhvat', models.CharField(choices=[('Територија Републике Србије', 'Територија Републике Србије'), ('Територија административне надлежности организације', 'Територија административне надлежности организације'), ('Друго', 'Друго')], max_length=100)),
                ('Razlog_nedostupnosti', models.CharField(choices=[('Цена', 'Цена'), ('Непостојање', 'Непостојање'), ('Неажурност', 'Неажурност'), ('Недоступност на интернету', 'Недоступност на интернету'), ('Начин преузимања', 'Начин преузимања'), ('Непокривеност', 'Непокривеност'), ('Непостојање дигиталне форме', 'Непостојање дигиталне форме'), ('Лоша садрадња са надлежном организацијом', 'Лоша садрадња са надлежном организацијом'), ('Тајност података', 'Тајност података'), ('Друго', 'Друго')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProstorniPodaci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Da_li_imate_potrebu_za_razmenm_prostornih_podataka', models.CharField(choices=[('Немамо искуства и потребе', 'Немамо искуства и потребе'), ('Немамо искуства, имамо потребе', 'Немамо искуства, имамо потребе'), ('Имамо искуства и потребе', 'Имамо искуства и потребе')], max_length=100)),
                ('Da_li_imate_kapaciteta_za_izradu_servisa', models.CharField(choices=[('Немамо капацитета, није у плану изградња капацитета', 'Немамо капацитета, није у плану изградња капацитета'), ('Немамо капацитета, у плану је изградња капацитета', 'Немамо капацитета, у плану је изградња капацитета'), ('Имамо капацитета, још увек не постоје креирани сервиси', 'Имамо капацитета, још увек не постоје креирани сервиси'), ('Имамо капацитета, постоје креирани сервиси', 'Имамо капацитета, постоје креирани сервиси')], max_length=100)),
                ('Dodatno_obrazovanje_u_okviru_organizacije', models.CharField(choices=[('Стандардизација геопроизвода и сервиса', 'Стандардизација геопроизвода и сервиса'), ('Дефинисање техничке спецификације за геоподатке', 'Дефинисање техничке спецификације за геоподатке'), ('Метаподаци', 'Метаподаци (креирање, стандардизације, израда каталога и сервиса)'), ('Израда web сервиса за геоподатке', 'Израда web сервиса за геоподатке'), ('Развој техничке инфраструктуре', 'Развој техничке инфраструктуре'), ('Креирања тематских речника', 'Креирања тематских речника'), ('Дефинисање политике размене, приступа и безбедности података', 'Дефинисање политике размене, приступа и безбедности података'), ('Друго', 'Друго')], max_length=100)),
                ('Nacin_razmene_podataka_sa_drugima', models.CharField(choices=[('Директно преузимање', 'Директно преузимање (дигитални медиј, папир)'), ('Преузимање преко интернета', 'Преузимање преко интернета (download: HTTP и FTP )'), ('Web сервиси', 'Web сервиси')], max_length=100)),
                ('Stav_o_razmeni_podataka', models.TextField()),
                ('Koje_prostorne_podatke_nabavljate_od_drugih', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.Pitanje3_3')),
                ('Odrediti_vazne_podatke_od_drugih_organizacija_za_redovne_aktivnosti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.Pitanje3_4')),
                ('Uneti_podatke_o_podacima_koje_vasa_organizacija_proizvodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.Pitanje3_2')),
                ('Za_koje_od_navedenih_INSPIRE_tema_proizvodite_podatke', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.Pitanje3_1')),
                ('Za_kojim_prostornim_podacima_imate_potrebu_a_koji_nisu_dostupni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitanja.Pitanje3_5')),
            ],
        ),
        migrations.RenameModel(
            old_name='KIadroviiInfrastruktura',
            new_name='KadroviInfrastruktura',
        ),
    ]
