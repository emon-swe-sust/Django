from django.urls import path
from . import views

urlpatterns = [
    path('kontact', views.kontact, name='kontact')
]
