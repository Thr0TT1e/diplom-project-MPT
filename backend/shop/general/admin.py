from django.contrib import admin
from .models import CardProduct, Category


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class CardProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'description', 'price', 'gender', 'size', 'image', 'date_publish', 'date_update')
	list_filter = ('date_publish', 'date_update', 'price', 'title')
	list_editable = ('price',)
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(CardProduct, CardProductAdmin)
