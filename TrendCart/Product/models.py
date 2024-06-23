from django.db import models
from Category.models import Subcategory
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    images = models.ImageField(upload_to="images/products", null=True, blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField()
    is_trending=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name