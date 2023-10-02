from django.shortcuts import render,get_object_or_404,redirect
from .models import Service,Site_services
from projects.models import Category

# Create your views here.

def services(request):
    category = Category.objects.all()
    service=Service.objects.filter(status=True)
    site=Site_services.objects.filter(status=True)
    context={
        'service':service,
        'site':site,
        'category':category,
    }
    return render(request,'service/services.html',context=context)



def service_detail(request,id):
        service=Service.objects.filter(status=True)
        try:
            service = Service.objects.get(id=id)
            context ={
                "service": service,
                }
            return render(request,'service/service-details.html',context=context)
        except:
                return render(request,'service/404.html')
    
