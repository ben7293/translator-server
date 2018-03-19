
from django.urls import path

from . import views

urlpatterns = [
    path('', views.translate, name='translate'),
    path('get_all/', views.getTranslationRecords, name='getTranslationRecords'),
]