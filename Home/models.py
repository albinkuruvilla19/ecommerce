from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150,null=False)
    image = models.ImageField(upload_to='uploads/',null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name
    
class Products(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False)
    seller = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to='uploads/',null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    orginal_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Products,on_delete=models.CASCADE)
    product_quantity = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.user.username}"



class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
