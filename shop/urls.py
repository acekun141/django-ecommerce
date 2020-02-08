from django.urls import path
from django.http import HttpResponse
from shop.views import HomePageView, ProductView, ShopView


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<int:pk>/', ProductView.as_view(), name='product')
]