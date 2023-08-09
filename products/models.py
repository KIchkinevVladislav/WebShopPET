from typing import Iterable, Optional

import stripe
from django.conf import settings
from django.db import models

from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY

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
    stripe_product_price_id = models.CharField(
        max_length=128, 
        null=True, blank=True,
        verbose_name='ID свойства price в базе Stripe'
        )
    category = models.ForeignKey(
        to=ProductCategory,
        on_delete=models.PROTECT,
        verbose_name='Категория товара'
        )    

    class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        # строковое отображение объекта
        return f'Продукт: {self.name} | Категория: {self.category.name}'
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields = None):
        # создание id товара хранящегося в Stripe в моделе
        if not self.stripe_product_price_id:
            stripe_product_prise = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_product_prise['id']
        return super(Product, self).save(force_insert, force_update, using, update_fields)
    
    def create_stripe_product_price(self):
        # создание продукта и его цены в базе Stripe
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'], 
            unit_amount=round(self.price * 100), 
            currency='rub'
            )
        return stripe_product_price


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)
    
    def stripe_products(self):
        # создание списка значений, содержаний данные о цене товара и количестве 
        # для обработки OrderCreateView
        # при передаче в checkout session Stripe
        line_items = []
        for basket in self:
            item = {
                'price': basket.product.stripe_product_price_id,
                'quantity': basket.quantity,
            }
            line_items.append(item)
        return line_items


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

    class Meta():
        verbose_name = 'Корзина с товарами'
        verbose_name_plural = 'Корзины с товарами'
    
    objects = BasketQuerySet.as_manager()
    
    def __str__(self):
        return f'Корзина для пользователя {self.user.username} | Товары: {self.product.name}'
    
    def sum(self):
        return self.product.price * self.quantity
    
    def de_json(self):
        # создаем json-объект для передачи данных в order.html
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }
        return basket_item
    