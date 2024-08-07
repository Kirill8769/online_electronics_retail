from django.contrib import admin

from product.models import Product


@admin.register(Product)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'release_date', )
    list_filter = ('vendor', )
    search_fields = ('title', )
