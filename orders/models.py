from django.db import models

from users.models import User

class Order(models.Model):
    """
    Модель, хранящая данные о заказе пользователя
    """
    # переменные для определения статуса доставки заказа
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    email = models.EmailField(max_length=256, verbose_name='Адрес электронной почты')
    adress = models.CharField(max_length=256, verbose_name='Адрес доставки')
    basket_history = models.JSONField(default=dict, verbose_name='Товары в доставке')
    created = models.DateTimeField(auto_created=True)
    staus = models.PositiveSmallIntegerField(default=CREATED, choices=STATUSES, verbose_name='Статус доставки товара')
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь, создавший заказ')    

    def __str__(self):
        return f'Order #{self.id}. {self.first_name} {self.last_name}.'
    
    class Meta():
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'