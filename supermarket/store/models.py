from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.IntegerField()
