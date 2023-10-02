from django.shortcuts import render,redirect
from .models import ContactUs, Order_Work,Constructions,Part,Team,Skills
from services.models import Service
from projects.models import Project,Category
from accounts.models import CustomeUser
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
        category=Category.objects.all()
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
    category=Category.objects.all()
    project_count = Project.objects.filter(status = True).count()
    engineer_count = Team.objects.filter(status = True).count()
    user_count = CustomeUser.objects.filter(is_active=True).count()
    team= Team.objects.filter(status=True)
    context={
        'team':team,
        'pc':project_count,
        'ec':engineer_count,
        'uc':user_count,
        'category':category,
    }

    return render(request,'root/about.html' , context=context)

def contact(request):
    if request.method == 'GET':
        category=Category.objects.all()
        context={
            'category':category,
        }
        return render(request,'root/contact.html',context=context)

        
    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submited successfully')
            return redirect('root:contact')
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:contact')