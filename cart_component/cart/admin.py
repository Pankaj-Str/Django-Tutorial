# cart/admin.py

from django.contrib import admin
from .models import CartItem

admin.site.register(CartItem)
