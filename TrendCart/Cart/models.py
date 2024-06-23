from django.db import models
from Product.models import Product
# from django.contrib.auth.models import User
from Accounts.models import CustomUser

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name
    def subtotal(self):
        return self.quantity*self.product.price

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     email = models.EmailField()
#     address = models.CharField(max_length=255)
#     address2 = models.CharField(max_length=255, blank=True, null=True)
#     country = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=20)
#     payment_method = models.CharField(max_length=50)
#     card_name = models.CharField(max_length=100)
#     card_number = models.CharField(max_length=20)
#     expiration = models.CharField(max_length=5)
#     cvv = models.CharField(max_length=4)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Order {self.id}"
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=100)
#     product_price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return f"{self.product_name} (x{self.quantity})"
#


# class Order(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f"Order {self.id} by {self.user.username}"
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f"{self.quantity} of {self.product.name}"

# Create your models here.
#
# class Order(models.Model):
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     no_of_items=models.IntegerField()
#     user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#     ordered_date=models.DateTimeField(auto_now_add=True)
#     address=models.TextField()
#     phone=models.TextField()
#     order_status=models.CharField(max_length=20,default="pending")
#     delivery_status=models.CharField(max_length=20,default="pending")
#     def __str__(self):
#         return self.product.name
#
# class Account(models.Model):
#     acctnum=models.IntegerField()
#     accttype=models.CharField(max_length=20)
#     amount=models.IntegerField()
#     def __str__(self):
#         return str(self.acctnum)



