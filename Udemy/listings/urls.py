from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='listings'),
    path('<int:listing_id>',views.listing, name='listng'),
    path('search',views.search,name='search'),
    path ('kontacts/',include('kontacts.urls')),
]