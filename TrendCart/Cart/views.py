from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Product.models import Product
from Cart.models import CartItem
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if created:
        if product.stock > 0:
            cart_item.quantity = 1
            cart_item.save()
        else:
            messages.error(request, "This product is out of stock.")
    else:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.error(request, "You have reached the maximum available stock for this product.")

    return redirect('Cart:cart')  #
@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_items_count = cart_items.count()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    in_stock_items = any(item.product.stock > 0 for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_items_count': cart_items_count,
        'in_stock_items': in_stock_items,
    })



@login_required
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    product = item.product

    if request.method == "POST":
        action = request.POST['action']
        if action == 'increase':
            if item.quantity < product.stock:
                item.quantity += 1
            else:
                messages.error(request, "Not enough stock available.")
        elif action == 'decrease' and item.quantity > 1:
            item.quantity -= 1
        item.save()

    return redirect('Cart:cart')


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return cart(request)

