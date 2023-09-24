from django.shortcuts import render,redirect
from .models import Order,ContactUs
from .forms import OrderForm,ContactUsForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request,'root/index.html')
    elif request.method == 'POST':
        form = OrderForm(request.POST)
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
            return redirect('root:home')
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:home')