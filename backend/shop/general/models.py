"""
models.py - в данном файле создаются объекты в базе данных.

class - ключевое слово для определения объектов. Имя объекта задаётся с большой буквы.
		Имя класса является названием таблицы в базе данных. Атрибуты (переменные), которые содержит класс являются
		полями в базе данных.
		Также, к имени объекта в скобках задаётся параметр (models.Model) с помощью которого система понимает,
		что объект сохраняется в базе данных.
"""

from django.db import models


class CardProduct(models.Model):
	SHIRT_SIZES = (
		('3T', '3 года'),
		('4T', '4 года'),
		('5T', '5 лет'),
		('6T', '6 лет'),
		('7T', '7 лет'),
	)
	GENDER = (
		('М', 'Мальчик'),
		('Д', 'Девочка'),
	)
	title = models.CharField(max_length=200)
	description = models.TextField()
	price = models.IntegerField()
	gender = models.CharField(max_length=1, choices=GENDER)
	image = models.ImageField(upload_to='%Y/%m/%d/')
	size = models.CharField(max_length=1, choices=SHIRT_SIZES)
	date_publish = models.DateField(auto_now_add=True)
