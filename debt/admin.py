from django.contrib import admin

from debt.models import Debt


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('id', 'debtor', 'borrower', 'amount', )
    list_filter = ('debtor', 'borrower', 'creation_date', )
    search_fields = ('debt', )
