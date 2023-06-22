from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=128, 
        unique=True, 
        verbose_name='Название категории'
        )
    description = models.TextField(
        null=True, 
        blank=True, 
        verbose_name='Описание категории'
        )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории товаров'
    

class Product(models.Model):
    name = models.CharField(
        max_length=256, 
        verbose_name='Название товара'
        )
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(
        max_digits=7, 
        decimal_places=2, 
        verbose_name='Стоимость товара'
        )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество товаров'
        )
    image = models.ImageField(
        upload_to='products_images',
        verbose_name='Изображение товара'
        )
    category = models.ForeignKey(
        to=ProductCategory, 
        on_delete=models.PROTECT,
        verbose_name='Категория товара'
        )
    
    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

    class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Basket(models.Model):
    user = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        verbose_name='Пользователь'
        )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='Товар'
        )
    quantity = models.PositiveSmallIntegerField(
        default=0, 
        verbose_name='Количество товаров'
        )
    created_timestamp = models.DateField(
        auto_now_add=True, 
        verbose_name='Дата создания'
        )
    
    def __str__(self):
        return f'Корзина для пользователя {self.user.username} | Товары: {self.product.name}'
    
    class Meta():
        verbose_name = 'Корзина с товарами'
        verbose_name_plural = 'Корзины с товарами'
    