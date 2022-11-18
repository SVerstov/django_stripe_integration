from django.conf.global_settings import MEDIA_ROOT
from django.db import models

bn = dict(blank=True, null=True)

currency_list = [('USD', 'Доллары США'), ('RUB', 'Рубли'), ('AMD', 'Армянский драм'), ('EUR', 'ЕВРО')]


class Item(models.Model):
    name = models.CharField('Наименования товара', max_length=256)
    description = models.TextField('Описание', **bn)
    # stripe_price_id = models.CharField()
    price = models.FloatField('Цена')
    currency = models.CharField('Валюта', blank=False, choices=currency_list, default='USD', max_length=10)
    photo = models.ImageField('Фото', upload_to=MEDIA_ROOT, default='default.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
