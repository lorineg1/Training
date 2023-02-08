from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length = 50)
    upload_date = models.DateField('Date Uploaded', default=timezone.now)
    price = models.IntegerField()
    image = models.ImageField(upload_to="shop/")
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('product-detail', args=[str(self.id)])

class User(AbstractBaseUser):
    id = models.CharField(max_length=5, null=False, unique=True, primary_key=True)
    full_name =  models.CharField(max_length=45, null=False)
    user_name =  models.CharField(max_length=45, null=True, default=full_name)
    phone_number = models.CharField(max_length=10, null=True)