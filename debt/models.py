from django.db import models

from company.models import Company


class Debt(models.Model):
    debtor = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        related_name='debtor',
        null=True,
        blank=True,
        verbose_name='Кто должен'
    )
    borrower = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        related_name='borrower',
        null=True,
        blank=True,
        verbose_name='Кому должен'
    )
    amount = models.FloatField(verbose_name='Сумма задолженности')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.debtor} - {self.borrower}'

    class Meta:
        ordering = ('id', )
        verbose_name = 'Задолженность'
        verbose_name_plural = 'Задолженности'

