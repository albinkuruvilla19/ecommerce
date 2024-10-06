from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('products/', ProductListCreateView.as_view(), name='product_list_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartListCreateView.as_view(), name='cart_list_create'),
    path('cart/<int:pk>/', CartDetailView.as_view(), name='cart_detail'),
    path('checkout/', CheckoutCreateView.as_view(), name='checkout_create'),
    path('login/', LoginAPI.as_view(), name="login_view")
   

]
