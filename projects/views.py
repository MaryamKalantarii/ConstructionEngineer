from django.shortcuts import render
from .models import Project,Category

# Create your views here.
def projects(request):
    project = Project.objects.filter(status=True)
    context={
        'project' : project,
    }
    return render(request,'project/projects.html',context=context)

def project_detail(request,id):
    project = Project.objects.get(id=id)
    projects = Project.objects.filter(status=True)
    category = Category.objects.all()
    context={
        'project' : project,
        'projects': projects,
        'category': category,
    }

    return render(request,'project/project-details.html',context=context)