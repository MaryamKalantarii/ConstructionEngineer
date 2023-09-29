from django.shortcuts import render
from .models import Service,Site_services

# Create your views here.

def services(request):
    service=Service.objects.filter(status=True)
    site=Site_services.objects.filter(status=True)
    context={
        'service':service,
        'site':site,
    }
    return render(request,'service/services.html',context=context)



def service_detail(request):
    # service = Service.objects.get(id=id)
    return render(request,'service/service-details.html')
