from django.db import models
from INVIGO.base_model import BaseCreatedUpdated


# Create your models here.
# Products
class Products(BaseCreatedUpdated):
    product_no=models.CharField(primary_key=True,max_length=20)
    name = models.TextField( max_length=200)
    quantity=models.IntegerField()
    price=models.FloatField()
    pescription=models.TextField(max_length=250)


class Supplier(BaseCreatedUpdated):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    gstin = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

class Purchase(BaseCreatedUpdated):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='purchasesupplier')


