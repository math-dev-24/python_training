
from django.contrib import admin
from django.urls import path
from appsimul.views import index, cacul

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home_page"),
    path('calcul', cacul , name="calcul"),
]
