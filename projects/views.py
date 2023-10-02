from django.shortcuts import render,get_object_or_404
from .models import Project,Category

# Create your views here.
def projects(request,cat=None):
    project = Project.objects.filter(status=True)
    context={
        'project' : project,
    }
    return render(request,'project/projects.html',context=context)

def project_detail(request,id):
    try:
        project = Project.objects.get(id=id)
        projects = Project.objects.filter(status=True)
        category = Category.objects.all()
        context={
            'project' : project,
            'projects': projects,
            'category': category,
        }

        return render(request,'project/project-details.html',context=context)
    except:
        return render(request,'service/404.html')


        