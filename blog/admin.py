from django.contrib import admin
from .models import Reply,Comment,Blog,Writer,Category

# Register your models here.

admin.site.register(Reply)
admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(Writer)
admin.site.register(Category)
