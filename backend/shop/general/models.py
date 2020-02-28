"""
models.py - в данном файле создаются объекты в базе данных.

class - ключевое слово для определения объектов. Имя объекта задаётся с большой буквы.
		Имя класса является названием таблицы в базе данных. Атрибуты (переменные), которые содержит класс являются
		полями в базе данных.
		Также, к имени объекта в скобках задаётся параметр (models.Model) с помощью которого система понимает,
		что объект сохраняется в базе данных.
"""

from django.db import models
from django.db.models import CASCADE
from django.utils import timezone

# Создаём объект, который определяет категорию товара


class Category(models.Model):
	title = models.CharField(max_length=60, verbose_name='Название категории', db_index=True)  # Наименование категории
	slug = models.SlugField(max_length=60, verbose_name='Алиас названия', db_index=True, unique=True)  # Алиас товара (
	# его URL)

	class Meta:
		ordering = ('title',)
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.title


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
	# Это отношение "Многие к одному" - товар относится к одной категории, а категория содержит несколько товаров
	category = models.ForeignKey(Category, verbose_name='Категория', related_name='products', on_delete=CASCADE)
	title = models.CharField(max_length=200, verbose_name='Наименование товара')  # Название товара
	description = models.TextField(verbose_name='Описание товара')  # Описание товара
	price = models.DecimalField(max_digits=7, verbose_name='Цена товара', decimal_places=2)  # Цена товара
	gender = models.CharField(max_length=2, choices=GENDER, verbose_name='Пол ребёнка')  # Пол ребёнка
	image = models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Фото товара', blank=True)  # Изображение товара
	size = models.CharField(max_length=2, choices=SHIRT_SIZES, verbose_name='Размер')  # Размер товара
	# available = models.BooleanField(default=True)  # Указывает доступен ли товара или нет.
	slug = models.SlugField(max_length=60, verbose_name='Алиас названия', db_index=True)  # Алиас товара (его URL)
	date_publish = models.DateField(auto_now_add=True, verbose_name='Дата публикации')  # Дата публикации/создания
	date_update = models.DateField(auto_now=True, verbose_name='Дата обновления')  # Дата обновления товара

	class Meta:
		verbose_name = 'Карточка продукта'
		verbose_name_plural = 'Карточка продукта'
		ordering = ('title',)
		index_together = (('id', 'slug'),)

	# def publish(self):
	# 	self.date_publish = timezone.now()
	# 	self.save()

	def __str__(self):
		return self.title
