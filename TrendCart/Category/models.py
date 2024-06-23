from django.db import models

# Create your models here.

class Maincategory(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    def __str__(self):
        return self.name
class Subcategory(models.Model):
    maincategory = models.ForeignKey(Maincategory, on_delete=models.CASCADE)
    sname=models.CharField(max_length=20)
    sdesc=models.TextField()
    simages=models.ImageField(upload_to="images/subcategory")

    def __str__(self):
        return self.sname