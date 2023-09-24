from django.db import models
from accounts.models import CustomeUser
import datetime


# Create your models here.

class Order (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    messege = models.TextField()

    def __str__(self):
        return self.name

class Constructions (models.Model):
    image = models.ImageField(upload_to="constructions",default='constructions.jpg')
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)






class Skills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Team(models.Model):
    info = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    image = models.ImageField(upload_to='engineer',default='engineer.jpg')
    twitter = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    linkdin = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.username



class ContactUs (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name


class Part(models.Model):
    part = models.CharField(max_length=100)
    image = models.ImageField(upload_to="part",default='part.jpg')
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
