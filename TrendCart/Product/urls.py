"""
URL configuration for TrendCart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Product import views
app_name="Product"
urlpatterns = [
    path('/addproduct',views.addproduct, name="addproduct"),
    path('/viewproducts',views.viewproducts,name="viewproducts"),
    path('/deleteproduct',views.deleteproduct,name="deleteproduct"),
    path('/delproduct/<int:p>', views.delproduct, name="delproduct"),
    path('/viewupdateproduct', views.viewupdateproduct, name="viewupdateproduct"),
    path('/updateproducts/<int:p>', views.updateproducts, name="updateproducts"),
    path('/updateproducts/updateproductrecord/<int:p>',views.updateproductrecord, name='updateproductrecord'),
    path('/productlist/', views.product_list, name='product_list'),
    # path('/mobilecomputer_productlist', views.mobilecomputer_productlist, name='mobilecomputer_productlist'),
    path('/tv_app_ele_productlist/<int:p>', views.tv_app_ele_productlist, name='tv_app_ele_productlist'),
    path('/product_detail/<int:p>', views.product_detail, name='product_detail'),
    path('admin/out_of_stock/', views.out_of_stock_products, name='out_of_stock_products'),

    # path('/trending_item/<int:p>', views.trending_item, name='trending_item'),


    # path('/addsubcategory', views.addsubcategory, name="addsubcategory"),
    # path('/viewsubcategory', views.viewsubcategory, name="viewsubcategory"),
    # path('/deletesubcategory', views.deletesubcategory, name="deletesubcategory"),
    # path('/delsubcategory/<int:p>', views.delsubcategory, name="delsubcategory"),
    # path('/viewupdatesubcategory', views.viewupdatesubcategory, name="viewupdatesubcategory"),
    # path('/updatesubcategory/<int:p>', views.updatesubcategory, name="updatesubcategory"),
    # path('/updatesubcategory/updatesubrecord/<int:p>', views.updatesubrecord, name='updatesubrecord'),

]
