from django.db import models
from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length = 50)

class Product(models.Model):
    name = models.CharField(max_length = 50)
    upload_date = models.DateField('Date Uploaded', default=timezone.now)
    price = models.IntegerField()
    id = models.IntegerField(primary_key= True)
    image = models.ImageField(upload_to="shop/")
    category = models.ForeignKey("Category",  on_delete=models.CASCADE) 

