from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path("",blog,name="blog"),
    path("blog-detail/<int:id>",blog_detail,name="blog_detail"),
    path("search/",blog ,name="blog_search"),
    path("comment/reply/<int:id>",reply,name="reply"),

    
]