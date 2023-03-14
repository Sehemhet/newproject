# Generated by Django 4.1.7 on 2023-03-10 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(db_index=True, default='', max_length=150, verbose_name='Бренд')),
                ('slug', models.SlugField(max_length=155, unique=True, verbose_name='URL')),
                ('logo', models.ImageField(upload_to='logo', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'ordering': ['brand'],
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Производитель')),
                ('flag', models.ImageField(upload_to='Country', verbose_name='Флаг')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производитель',
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='TypeClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Класс',
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='TypeDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Тип привода')),
            ],
            options={
                'verbose_name': 'Привод',
                'verbose_name_plural': 'Привод',
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='TypeEngine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Тип двигателя')),
            ],
            options={
                'verbose_name': 'Двигатель',
                'verbose_name_plural': 'Двигатель',
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='TypeRarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Редкость')),
            ],
            options={
                'verbose_name': 'Редкость',
                'verbose_name_plural': 'Редкость',
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=150, verbose_name='Модель')),
                ('year', models.PositiveSmallIntegerField(blank=True, verbose_name='Год')),
                ('slug', models.SlugField(default='', max_length=255, unique=True, verbose_name='URL')),
                ('level', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Уровень')),
                ('price', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Цена')),
                ('speed', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Скорость')),
                ('control', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Управление')),
                ('acceleration', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Ускорение')),
                ('start', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Разгон')),
                ('brake', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Торможение')),
                ('kW', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='кВт')),
                ('Hp', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Л.с.')),
                ('Hm', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Н/м')),
                ('weight', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Вес')),
                ('center', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Фронтальная нагрузка')),
                ('volume', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='Объем')),
                ('top_speed', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='макс. скорость')),
                ('start097', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='0-97км/ч')),
                ('start161', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='0-161км/ч')),
                ('brake097', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='97-0 км/ч')),
                ('brake161', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='161-0 км/ч')),
                ('load97', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='нагрузка 97 км/ч')),
                ('load193', models.PositiveSmallIntegerField(blank=True, default=True, verbose_name='нагрузка 193 км/ч')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='cars/%Y/%m/%d', verbose_name='Фото')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auto.brands', verbose_name='Бренд')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auto.county', verbose_name='Производитель')),
                ('rarity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auto.typerarity', verbose_name='Редкость')),
                ('type_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auto.typeclass', verbose_name='Класс')),
                ('type_drive', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auto.typedrive', verbose_name='Тип привода')),
                ('type_engine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auto.typeengine', verbose_name='Тип двигателя')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
                'ordering': ['brand', 'model', 'year'],
            },
        ),
    ]
