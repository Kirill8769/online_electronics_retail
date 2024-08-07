from django.contrib import admin

from company.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'entity', 'country', 'city', 'vendor', )
    list_filter = ('entity', 'country', 'city', 'creation_date', )
    search_fields = ('city', )
