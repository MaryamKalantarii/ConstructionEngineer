from django.urls import path
from .views import *

app_name = 'projects'

urlpatterns = [
    path("",projects,name="projects"),
    path("category/<str:cat>",projects,name ="project_cat"),
    path("project-detail/<int:id>",project_detail,name="project_detail"),
    
    
]