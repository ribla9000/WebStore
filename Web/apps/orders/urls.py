from django.urls import path
from . import views


# app_name = 'orders'
urlpatterns = [
    
    
    path(r'^in_shopcart/$', views.in_shopcart, name = 'in_shopcart'),

]


