from django.db import models

class BaseCreatedUpdated(models.Model):
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True