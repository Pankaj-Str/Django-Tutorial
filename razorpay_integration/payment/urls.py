from django.urls import path
from .views import initiate_payment, complete_payment

urlpatterns = [
    path('pay/', initiate_payment, name='initiate_payment'),
    path('complete/', complete_payment, name='complete_payment'),
]
