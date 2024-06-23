from django.shortcuts import render, redirect, get_object_or_404
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from Order.models import Order,OrderItem
from Accounts.models import CustomUser
from Cart.models import CartItem
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

@login_required
def place_order(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_amount = sum(item.subtotal() for item in cart_items)
    total_quantity = sum(item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
        'total_quantity': total_quantity,
    }
    if request.method == 'POST':
        u = request.user
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        address = request.POST['address']
        address2 = request.POST['address2']
        country = request.POST['country']
        state = request.POST['state']
        zip_code = request.POST['zip']
        payment_method = request.POST['paymentMethod']
        card_name = request.POST['cc-name']
        card_number = request.POST['cc-number']
        expiration = request.POST['cc-expiration']
        cvv = request.POST['cc-cvv']

        order = Order.objects.create(
            user=u,
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            address2=address2,
            country=country,
            state=state,
            zip_code=zip_code,
            payment_method=payment_method,
            card_name=card_name,
            card_number=card_number,
            expiration=expiration,
            cvv=cvv
        )

        # Send confirmation email to user
        subject = 'Order Confirmation'
        html_message = render_to_string('order_confirmation_email.html', {'user': request.user, 'order': order})
        plain_message = f"Dear {request.user.first_name}, Your order has been placed successfully."
        from_email = settings.EMAIL_HOST_USER
        to_email = [request.user.email]

        try:
            send_mail(subject, plain_message, from_email, to_email, html_message=html_message)

        except Exception as e:

            print(f"Error sending email: {e}")

        # Iterate over cart items and create order items
        for cart_item in cart_items:
            product = cart_item.product
            OrderItem.objects.create(
                order=order,
                product_name=product.name,
                product_price=product.price,
                quantity=cart_item.quantity
            )
            # Decrease the product stock
            product.stock -= cart_item.quantity
            product.save()

        # Clear the cart
        CartItem.objects.filter(user=user).delete()
        return order_success(request, order.id)

    return render(request, 'place_order.html', context)

def order_success(request, order_id):
    order = Order.objects.get(id=order_id)
    # oi=OrderItem.objects.get(id=order_id)
    estimated_delivery_date = order.created_at + timedelta(days=5)
    context = {
        'order': order,
        'estimated_delivery_date': estimated_delivery_date,


    }
    return render(request, 'order_success.html', context)
@login_required
def order_history(request):
    user = request.user
    order_items = OrderItem.objects.filter(order__user=user).order_by('-order_date')
    return render(request, 'order_history.html', {'order_items': order_items})

def order_list(request):
    orders = Order.objects.all()
    context = {
            # 'order_items': order_items,
            'orders': orders,
        }

    return render(request, 'order_list.html', context)

# def order_list(request):
#     orders = Order.objects.all()
#     return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, p):
    order = get_object_or_404(Order, id=p)
    # return render(request, 'order_detail.html')
    return render(request, 'order_detail.html', {'order': order})

def order_view(request,p):
    order = get_object_or_404(Order, id=p)
    # return render(request, 'order_detail.html')
    return render(request, 'update_order_status.html', {'order': order})
def update_order_status(request,p):
    if(request.method=="POST"):
        orderdb = Order.objects.get(id=p)
        order_status=request.POST['order_status']
        orderdb.order_status=order_status
        # order=Order.objects.create(order_status=order_status)
        orderdb.save()
        return order_list(request)
    return render(request, 'order_list.html')









