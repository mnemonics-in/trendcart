from django.shortcuts import render,get_object_or_404
from Category.models import Maincategory
from Category.models import Subcategory
from Product.models import Product
from Cart.models import CartItem
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import  login_required
from django.shortcuts import render, redirect
from django.template import loader
from django.db.models import Q
from django.core.paginator import Paginator
from .filters import ProductFilter

# Create your views here.
@login_required
def addproduct(request):
    sc = Subcategory.objects.all()
    if (request.method == "POST"):
        product_name = request.POST['product_name']
        product_description = request.POST['product_description']
        product_image = request.FILES['product_image']
        product_price = request.POST['product_price']
        product_category_id = request.POST['product_category']
        product_stock = request.POST['product_stock']
        product_available = request.POST['product_available']
        product_category = Subcategory.objects.get(id=product_category_id)

        # product_create_date = request.POST['product_create_date']
        # product_updated = request.POST['product_updated']
        p = Product.objects.create(name=product_name, desc=product_description,images=product_image,price=product_price,subcategory=product_category,stock=product_stock,available=product_available)
        p.save()
        return viewproducts(request)
    return render(request,template_name="addproduct.html",context={'sc':sc})
def viewproducts(request):
    vp=Product.objects.all()

    return render(request,template_name="viewproducts.html",context={'vp':vp})

def viewupdateproduct(request):
    vp = Product.objects.all()

    return render(request, template_name='viewupdateproduct.html', context={'vp': vp})

def updateproducts(request,p):
    vp= Product.objects.get(id=p)
    template = loader.get_template('updateproduct.html')
    context = {'vp': vp}
    return HttpResponse(template.render(context, request))

def updateproductrecord(request, p):
    product_name = request.POST['product_name']
    product_description = request.POST['product_description']
    # product_image = request.FILES['product_image']
    product_price = request.POST['product_price']
    # product_category_id = request.POST['product_category']
    product_stock = request.POST['product_stock']
    product_available = request.POST['product_available']
    up = Product.objects.get(id=p)
    up.name=product_name
    up.desc=product_description
    # up.images=product_image
    up.price=product_price
    up.stock=product_stock
    up.available=product_available
    up.save()
    return viewupdateproduct(request)
def deleteproduct(request):
    dp = Product.objects.all()

    return render(request, template_name='deleteproduct.html', context={'dp': dp})

def delproduct(request,p):
    b=Product.objects.get(id=p)
    b.delete()
    return deleteproduct(request)


def product_list(request):
    products = Product.objects.all()
    categories = Subcategory.objects.all()

    # Filtering
    category_id = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if category_id:
        products = products.filter(subcategory_id=category_id)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Pagination
    paginator = Paginator(products, 9)  # Show 9 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
    }

    return render(request, 'product_list.html', context)
# -----------------User View----------------

def tv_app_ele_productlist(request,p):
    category = get_object_or_404(Maincategory, id=p)
    sub_categories = Subcategory.objects.filter(maincategory=category)
    products = Product.objects.filter(subcategory__in=sub_categories)

    sub_category_id = request.GET.get('sub_category')
    if sub_category_id:
        products = products.filter(subcategory=sub_category_id)

    paginator = Paginator(products, 10)  # Show 10 products per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'sub_categories': sub_categories,
        'products': page_obj,
    }
    return render(request, 'tv_appliances_electronics.html', context)

def product_detail(request,p):
    d = Product.objects.get(id=p)
    cart_item = CartItem.objects.filter(user=request.user, product=d).first() if request.user.is_authenticated else None
    return render(request,template_name='product_detail.html',context={'product':d, 'cart_item': cart_item,})

def out_of_stock_products(request):
    out_of_stock_products = Product.objects.filter(stock=0)
    context = {
        'out_of_stock_products': out_of_stock_products
    }
    return render(request, 'out_of_stock_products.html', context)