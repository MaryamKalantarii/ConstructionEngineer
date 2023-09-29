from django.shortcuts import render,redirect
from .models import ContactUs, Order_Work,Constructions,Part
from services.models import Service
from projects.models import Project,Category
from blog.models import Blog
from .forms import ContactUsForm, Order_WorkForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'GET':
        blog= Blog.objects.filter(status=True)
        part = Part.objects.filter(status=True)
        conts = Constructions.objects.filter(status=True)
        service=Service.objects.filter(status=True)
        project=Project.objects.filter(status=True)
        category = Category.objects.all()
        context={
            'blog':blog,
            'category':category,
            'conts': conts,
            'service': service,
            'part': part,
            'project':project
        }
        return render(request,'root/index.html',context=context)
    elif request.method == 'POST':
        form = Order_WorkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submited successfully')
            return redirect('root:home')
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:home')

def about(request):
    return render(request,'root/about.html')

def contact(request):
    if request.method == 'GET':
        return render(request,'root/contact.html')
    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submited successfully')
            return redirect('root:contact')
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:contact')