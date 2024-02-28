# cart/urls.py

from django.urls import path
from .views import update_cart, display_cart, remove_from_cart

urlpatterns = [
    path('update_cart/', update_cart, name='update_cart'),
    path('cart/', display_cart, name='cart_display'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
]
