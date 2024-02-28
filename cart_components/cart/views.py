# cart/views.py

from django.shortcuts import render, redirect
from .models import CartItem

def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        price = float(request.POST.get('price'))

        # Check if item already exists in cart
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product_id=product_id,
            price=price
        )

        # If item exists, update quantity; otherwise, create new cart item
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

    return redirect('cart_display')

def display_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.subtotal() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart_display')
