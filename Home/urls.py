from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', category_list_create, name='category_list_create'),
    path('categories/<int:pk>/',category_detail, name='category_detail'),
    path('products/', product_list_create, name='product_list_create'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('cart/', cart_list_create, name='cart_list_create'),
    path('cart/<int:pk>/', cart_detail, name='cart_detail'),
    path('checkout/', checkout_create, name='checkout_create'),
    path('login/',login_api , name="login_view")
]
