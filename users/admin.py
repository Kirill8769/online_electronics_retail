from django.contrib import admin

from users.models import User


@admin.register(User)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_active', 'is_superuser', )
    list_filter = ('is_active', 'is_superuser', )
    search_fields = ('username', )
