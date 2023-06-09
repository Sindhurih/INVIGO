from django.db import models


# Create your models here.

class User(models.Model):
    email_id = models.CharField(primary_key=True, max_length=200)
    password = models.TextField()

