from django.db import models
from django.contrib.auth.models import User

class Gender(models.Model):
    genderName=models.CharField(max_length=100)

class Shoe(models.Model):
    name=models.CharField(max_length=100)
    genderId=models.ForeignKey(Gender, on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    description=models.TextField(default='')
    color=models.CharField(max_length=100)
    image=models.ImageField(upload_to='shoes',default='shoes/default.png')

class Order(models.Model):
    userId=models.ForeignKey(User, on_delete=models.CASCADE)
    orderNumber=models.IntegerField()

class Size(models.Model):
    shoeId=models.ForeignKey(Shoe, on_delete=models.CASCADE)
    sizeNumb = models.IntegerField(default=0)
    sizeAmount=models.PositiveIntegerField(default=0)

class OrderShoe(models.Model):
    orderNumber=models.IntegerField()
    shoeId=models.ForeignKey(Shoe,on_delete=models.CASCADE)
    sizeId=models.ForeignKey(Size,on_delete=models.CASCADE)

class Contact(models.Model):
    userId=models.ForeignKey(User, on_delete=models.CASCADE)
    contactName=models.CharField(max_length=100)
    contactSubject=models.CharField(max_length=100)
    contactEmail=models.EmailField()
    contactMessage=models.TextField()







