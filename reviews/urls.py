# Defines what views different urls point to
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name='index2'),
    path('restaurants/', views.RestaurantList, name='restaurants'),
    path('search/', views.RestaurantSearch, name='restaurant-search'),
    path('account/', views.Account, name='account'),
    path('restaurants/<int:restaurant_id>', views.RestaurantDetails, name='restaurant-detail'),
    path('about',views.About, name ='about'),
    path('cafes', views.Cafes, name='cafes'),

]

urlpatterns += staticfiles_urlpatterns()