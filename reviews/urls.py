# Defines what views different urls point to
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name='index2'),
    path('restaurants/', views.RestaurantList, name='restaurants'),
    path('restaurants/<int:restaurant_id>', views.RestaurantDetails, name='restaurant-detail'),
]

urlpatterns += staticfiles_urlpatterns()