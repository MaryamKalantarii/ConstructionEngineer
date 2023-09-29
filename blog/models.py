from django.db import models
from accounts.models import CustomeUser
import datetime





class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class Writer(models.Model):
    info = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.username
    
    


class Blog(models.Model):
    image = models.ImageField(upload_to='blog',default='default.jpg')
    image2 = models.ImageField(upload_to='blog',default='default.jpg')
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200,default=False)
    title3 = models.CharField(max_length=200,default=False)
    content = models.TextField()
    content2 = models.TextField(default=False)
    content3 = models.TextField(default=False)
    content4 = models.TextField(default=False)
    writer = models.ForeignKey(Writer,on_delete=models.CASCADE)
    schedule = models.DateTimeField(default=datetime.datetime.now())
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title



class Comment(models.Model):
    which_blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name

class Reply(models.Model):
    which_comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name