from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=250, verbose_name='название товара')
    description = models.TextField(verbose_name='описание товара', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='стоимость товара')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'