from django.db import models

# Create your models here.
class Products(models.Model):
    Product_No=models.CharField(primary_key=True,max_length=20)
    Name = models.TextField( max_length=200)
    Quantity=models.IntegerField()
    Price=models.FloatField()
    Description=models.TextField(max_length=250)

