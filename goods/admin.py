from django.contrib import admin

# Register your models here.
# Здесь може добавлять модели(базы данных) что они были видны в адимнке

from goods.models import Categories
from goods.models import Product

#admin.site.register(Categories) #Регистрируем в админку модель Categories
#admin.site.register(Product)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}# В данной строке происходит автоматическое заполнение переменной slug для url странички


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}# В данной строке происходит автоматическое заполнение переменной slug для url странички 