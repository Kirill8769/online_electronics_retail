from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('company.urls', namespace='company')),
    path('product/', include('product.urls', namespace='product')),
    path('debt/', include('debt.urls', namespace='debt')),
]
