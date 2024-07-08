
from django.db import models
#

# Создаём свою модель(таблицу) баз данных с полями имя, url, id - создаётся автоматически
 
# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length = 150, unique = True, verbose_name = "Имя")
    slug = models.SlugField(max_length = 200, unique = True, blank = True, null = True, verbose_name = "Название сайта")
    
    # Класс Мета нужен для настройки нашей модели
    class Meta:
        # Изначально Django перед именем в таблице а оно берется из class ->Categories<-(models.Model) добавит goods 
        db_table = "category"  # Здесь мы укажем имя в 1-ным числе
        
        verbose_name = "Категория"# Здесь записываем в единственном числе
        verbose_name_plural = "Категории"#Записываем как она будет видна в админке пишем во множественном числе

    
    #Перегружаем магический метод __str__() для того чтобы в админке быле все красиво
    def __str__(self)->str:
        return self.name # Мы просто возвращаем имя написанае ранее


class Product(models.Model):
    name = models.CharField(max_length = 150 , unique = True, null = True, verbose_name = "Имя")
    slug = models.SlugField(max_length = 200, unique = True, null = True, blank = True, verbose_name = "URL")
    descriptions = models.TextField(null = True, unique = True, verbose_name = "Описание" )
    image = models.ImageField(upload_to = "goods_images", null = True, blank = True, verbose_name = "Картинка")
    price = models.DecimalField(default = 0.00, max_digits = 7, decimal_places = 2, verbose_name = "Цена")
    sale = models.DecimalField(default = 0.00, max_digits = 4, decimal_places = 2, verbose_name= "Скидка")
    count = models.PositiveIntegerField(default = 0, verbose_name = "Количество")
    # Тут мы связываем таблицы ы с друг с другом этой таблицы с Категорией 
    category = models.ForeignKey(to = Categories, on_delete = models.CASCADE, verbose_name = "Категория") #  on_delete(при удалении) 
    #PROTECTED(не разрешать удалять категорию если там есть товары),
    #SET_DEFAULT(при удалении товара будет присвоино ссылка по умалчанию и потом мы указываем ссылку), 
    #CASCADE(можемь удалить категорию даже если там есть товары нас просто предупредять в админке)

    class Meta:
        db_table = "product"

        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name