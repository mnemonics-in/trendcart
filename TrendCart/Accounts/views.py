from django.shortcuts import render,redirect
from Accounts.models import CustomUser
from django.contrib import messages
from django.conf import settings  # Import settings module
from django.core.mail import send_mail  # Import send_mail function
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from Product.models import Product
from Order.models import Order
from django.contrib.auth import update_session_auth_hash
def index(request):
    trending_items = Product.objects.filter(is_trending=True)
    paginator = Paginator(trending_items, 6)  # Show 6 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context)

def signup(request):
    if request.method == "POST":
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phonenumber']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirmPassword']

        if password == cpassword:
            # Check if the username already exists
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('Accounts:signup')

            # Check if the email already exists
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already in use.')
                return redirect('Accounts:signup')

            try:
                # Create user
                user = CustomUser.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    email=email,
                    username=username,
                    password=password,
                    phone=phone
                )
                user.save()

                # Send welcome email
                subject = 'Welcome to TrendCart!'
                message = f"""
                Hi {user.first_name},

                Welcome to TrendCart! 

                Thank you for registering on our website. We're thrilled to have you on board and can't wait for you to explore the latest products and deals we have to offer.

                Here are a few things you can do now:
                - Browse our wide selection of products
                - Enjoy exclusive discounts and offers

                If you have any questions or need assistance, feel free to reach out to our customer support team at support@trendcart.com.

                Happy shopping!

                Best regards,
                The TrendCart Team
                trendcart.com
                """
                from_email = settings.EMAIL_HOST_USER
                to_email = [user.email]

                send_mail(subject, message, from_email, to_email, fail_silently=True)

                # Display success message and redirect to login page
                messages.success(request, 'Account created successfully')
                return redirect('Accounts:login')

            except IntegrityError:
                messages.error(request, 'An error occurred during registration. Please try again.')
                return redirect('Accounts:signup')

        else:
            # Passwords do not match
            messages.error(request, 'Passwords do not match.')
            return redirect('Accounts:signup')

    return render(request, 'signup.html')


# views.py


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('Accounts:admin_dashboard')  # Redirect admin to admin home page
            else:
                login(request, user)
                return redirect('Accounts:index')  # Redirect user to user home page
        else:
            # Return an error message or handle invalid login
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required
def user_logout(request):
     logout(request)
     return redirect('Accounts:login')

def admin_dashboard(request):
    total_users = CustomUser.objects.filter(is_superuser=False).count()
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    pending_orders = Order.objects.filter(order_status='Pending').count()
    out_of_stock_products = Product.objects.filter(stock=0).count()

    context = {
        'total_users': total_users,
        'total_orders': total_orders,
        'total_products': total_products,
        'pending_orders': pending_orders,
        'out_of_stock_products': out_of_stock_products,
    }
    return render(request, 'admin_dashboard.html', context)
def user_home(request):

    return render(request,template_name='index.html')
    # return render(request,template_name='userdash.html')

@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    users = CustomUser.objects.all()

    return render(request,template_name='viewuserslist.html',context={'users':users})
#
@user_passes_test(lambda u: u.is_superuser)
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request,template_name='userdetail.html',context={'user': user})
@user_passes_test(lambda u: u.is_superuser)
def deactivate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_active = False
    user.save()
    return redirect('Accounts:user_list')
@user_passes_test(lambda u: u.is_superuser)
def activate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_active = True
    user.save()
    return redirect('Accounts:user_list')

@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect('Accounts:user_list')

def about_us(request):

    return render(request,template_name='about_us.html')
def contact_us(request):

    return render(request,template_name='contact_us.html')
@login_required
def profile(request):

    return render(request,template_name='profile.html')
@login_required
def update_profile(request,p):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    phone=request.POST['phone']
    u=CustomUser.objects.get(id=p)
    u.first_name=first_name
    u.last_name=last_name
    u.email=email
    u.phone=phone
    u.save()
    messages.success(request,'Profile updated successfully.')
    return redirect('Accounts:profile')


def change_password(request,p):
    current_password=request.POST['current_password']
    new_password=request.POST['new_password']
    u = CustomUser.objects.get(id=p)
    if not request.user.check_password(current_password):
        messages.error(request, 'Current password is incorrect.')
    else:
        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)  # Important!
        messages.success(request, 'Password changed successfully.')
        return redirect('Accounts:profile')
    return redirect('Accounts:profile')