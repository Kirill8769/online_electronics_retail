from django.db import models

from company.models import Company


class Product(models.Model):
    """Модель товара."""

    title = models.CharField(max_length=150, verbose_name='Название')
    model = models.CharField(max_length=150, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')
    vendor = models.ManyToManyField(Company, verbose_name='Поставщик')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id', )
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
