from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_add, name='show_add'),
    path('update', views.update, name='update'),
]
