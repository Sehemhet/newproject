import os
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
import pytils.translit


class Cars(models.Model):
	brand = models.ForeignKey('Brands', on_delete=models.PROTECT, verbose_name='Бренд')
	model = models.CharField(max_length=150, verbose_name='Модель')
	year = models.PositiveSmallIntegerField(blank=True, verbose_name='Год')
	slug = models.SlugField(max_length=255, unique=True, default='', null=False, db_index=True, verbose_name='URL')

	level = models.PositiveSmallIntegerField(blank=True, verbose_name='Уровень')
	country = models.ForeignKey('County', on_delete=models.PROTECT, verbose_name='Производитель')
	type_drive = models.ForeignKey('TypeDrive', on_delete=models.PROTECT, verbose_name='Тип привода')
	rarity = models.ForeignKey('TypeRarity', on_delete=models.PROTECT, verbose_name='Редкость')
	type_engine = models.ForeignKey('TypeEngine', on_delete=models.PROTECT, verbose_name='Тип двигателя')
	type_class = models.ForeignKey('TypeClass', on_delete=models.PROTECT, verbose_name='Класс')
	price = models.PositiveSmallIntegerField(blank=True, verbose_name='Цена')
	speed = models.PositiveSmallIntegerField(blank=True, verbose_name='Скорость')
	control = models.PositiveSmallIntegerField(blank=True, verbose_name='Управление')
	acceleration = models.PositiveSmallIntegerField(blank=True, verbose_name='Ускорение')
	start = models.PositiveSmallIntegerField(blank=True, verbose_name='Разгон')
	brake = models.PositiveSmallIntegerField(blank=True, verbose_name='Торможение')

	kW = models.PositiveSmallIntegerField(blank=True, verbose_name='кВт')
	Hp = models.PositiveSmallIntegerField(blank=True, verbose_name='Л.с.')
	Hm = models.PositiveSmallIntegerField(blank=True, verbose_name='Н/м')
	weight = models.PositiveSmallIntegerField(blank=True, verbose_name='Вес')
	center = models.PositiveSmallIntegerField(blank=True, verbose_name='Фронтальная нагрузка')
	volume = models.PositiveSmallIntegerField(blank=True, verbose_name='Объем')

	top_speed = models.PositiveSmallIntegerField(blank=True, verbose_name='макс. скорость')
	start097 = models.PositiveSmallIntegerField(blank=True, verbose_name='0-97км/ч')
	start161 = models.PositiveSmallIntegerField(blank=True, verbose_name='0-161км/ч')
	brake097 = models.PositiveSmallIntegerField(blank=True, verbose_name='97-0 км/ч')
	brake161 = models.PositiveSmallIntegerField(blank=True, verbose_name='161-0 км/ч')
	load97 = models.PositiveSmallIntegerField(blank=True, verbose_name='нагрузка 97 км/ч')
	load193 = models.PositiveSmallIntegerField(blank=True, verbose_name='нагрузка 193 км/ч')
	photo = models.ImageField(upload_to='cars/%Y/%m/%d', verbose_name='Фото', null=True, blank=True)

	def __str__(self):
		return self.model

	def get_absolute_url(self):
		return reverse('cars', kwargs={
			'slug': self.slug
		})

	# def save(self, *args, **kwargs):
	# 	self.slug = pytils.translit.translify(slugify(self.model, self.year, allow_unicode=True))
	# 	super().save(*args, **kwargs)

	def get_absolute_image(self):
		return os.path.join('/media/logo', self.slug)

	class Meta:
		verbose_name = 'Автомобиль'
		verbose_name_plural = 'Автомобили'
		ordering = ['brand','model','year']

class Brands(models.Model):
	brand = models.CharField(max_length=150, db_index=True, default='', null=False, verbose_name='Бренд')
	slug = models.SlugField(max_length=155, unique=True, db_index=True, verbose_name='URL')
	logo = models.ImageField(upload_to='logo', verbose_name='Логотип')

	def __str__(self):
		return self.slug

	def get_absolute_url(self):
		return reverse('brands', kwargs={
			'slug': self.slug
		})

	class Meta:
		verbose_name = 'Бренд'
		verbose_name_plural = 'Бренды'
		ordering = ['brand']

class TypeDrive(models.Model):
	type = models.CharField(max_length=50, verbose_name='Тип привода')

	def __str__(self):
		return self.type

	class Meta:
		verbose_name = 'Привод'
		verbose_name_plural = 'Привод'
		ordering = ['type']

class TypeEngine(models.Model):
	type = models.CharField(max_length=50, verbose_name='Тип двигателя')

	def __str__(self):
		return self.type

	class Meta:
		verbose_name = 'Двигатель'
		verbose_name_plural = 'Двигатель'
		ordering = ['type']

class TypeRarity(models.Model):
	type = models.CharField(max_length=50, verbose_name='Редкость')

	def __str__(self):
		return self.type

	class Meta:
		verbose_name = 'Редкость'
		verbose_name_plural = 'Редкость'
		ordering = ['type']

class County(models.Model):
	type = models.CharField(max_length=50, verbose_name='Производитель')
	flag = models.ImageField(upload_to='Country', verbose_name='Флаг')

	def __str__(self):
		return self.type

	class Meta:
		verbose_name = 'Производитель'
		verbose_name_plural = 'Производитель'
		ordering = ['type']

class TypeClass(models.Model):
	type = models.CharField(max_length=50, verbose_name='Класс')

	def __str__(self):
		return self.type

	class Meta:
		verbose_name = 'Класс'
		verbose_name_plural = 'Класс'
		ordering = ['type']


