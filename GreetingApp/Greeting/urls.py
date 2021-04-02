from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.create_user, name='index'),
    path('show', views.show, name='show'),
    path('update/<int:id>', views.update, name='update'),
]
