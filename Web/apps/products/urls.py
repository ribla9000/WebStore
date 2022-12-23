from django.urls import path
from . import views




# app_name = 'products'
urlpatterns = [
    
    path(r'^product/(?P<product_id>\w+/$)', views.product, name = 'product'),
    # path('shopingcart/', views.shoping_cart, name = 'shoping_cart'),
    
#     path('<int:article_id>/', views.detail, name = 'detail'),
#     path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
    

]


