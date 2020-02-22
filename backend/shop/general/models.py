"""
models.py - в данном файле создаются объекты в базе данных.

class - ключевое слово для определения объектов. Имя объекта задаётся с большой буквы.
		Имя класса является названием таблицы в базе данных. Атрибуты (переменные), которые содержит класс являются
		полями в базе данных.
		Также, к имени объекта в скобках задаётся параметр (models.Model) с помощью которого система понимает,
		что объект сохраняется в базе данных.
"""

from django.db import models
from django.utils import timezone


class CardProduct(models.Model):
	SHIRT_SIZES = [
		('3T', '3 года'),
		('4T', '4 года'),
		('5T', '5 лет'),
		('6T', '6 лет'),
		('7T', '7 лет'),
	]
	GENDER = [
		('М', 'Мальчик'),
		('Д', 'Девочка'),
	]
	title = models.CharField(max_length=200, verbose_name='Наименование товара')
	description = models.TextField(verbose_name='Описание товара')
	price = models.IntegerField(verbose_name='Цена товара')
	gender = models.CharField(max_length=2, choices=GENDER, verbose_name='Пол ребёнка')
	image = models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Фото товара')
	size = models.CharField(max_length=2, choices=SHIRT_SIZES, verbose_name='Размер')
	date_publish = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = 'Карточка продукта'
		verbose_name_plural = 'Карточка продукта'

	def publish(self):
		self.date_publish = timezone.now()
		self.save()

	def __str__(self):
		return self.title
