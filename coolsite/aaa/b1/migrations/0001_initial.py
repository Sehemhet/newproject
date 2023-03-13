# Generated by Django 4.1.7 on 2023-03-01 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Фио')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Изменение')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='b1.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Женщины',
                'verbose_name_plural': 'Женщины',
                'ordering': ['-time_create'],
            },
        ),
    ]
