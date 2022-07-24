from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('<int:shenasepardakht>/', views.sfapi, name='sfapi'),
]
