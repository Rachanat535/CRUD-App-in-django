from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length = 100)
    quantity = models.IntegerField()
    unitprice = models.IntegerField()
    stockcode = models.CharField(max_length = 10)
