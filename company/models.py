from django.db import models


class Company(models.Model):
    """Модель компании."""

    ENTITY_LIST = [
        ('factory', 'Завод'),
        ('retail', 'Розничная сеть'),
        ('individual', 'Индивидуальный предприниматель')
    ]

    name = models.CharField(max_length=150, verbose_name='Название')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    entity = models.CharField(max_length=15, choices=ENTITY_LIST, verbose_name='Форма организации')
    vendor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Поставщик')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id', )
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
