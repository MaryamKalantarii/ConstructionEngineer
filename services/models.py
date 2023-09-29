from django.db import models

# Create your models here.

class Service(models.Model):
    image = models.ImageField(upload_to="service",default='service.jpg')
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title

class Site_services(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    
