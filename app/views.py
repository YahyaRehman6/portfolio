from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import Form
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Profile_Picture

def home(request):
    return render(request,'app/home.html')

def about(request):
    image = Profile_Picture.objects.earliest('image')
    print(image)
    return render(request,'app/about.html',{'image':image})

def projects(request):
    return render(request,'app/projects.html')

from django.http import HttpResponse
from .tasks import send_email
def contact(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            try:
                message = form.cleaned_data['message']
                email = form.cleaned_data['email']
                name = form.cleaned_data['name']
                
                overall_message = f"Yahya a message is received from {name} \n Email is : {email} \n And message is \n \"{message}\""
                form.save()
                send_email.delay(overall_message)
                messages.success(request,"Message Sent")
                return HttpResponseRedirect('/contact/')
            except Exception as e :
                print(e)
                return HttpResponse(e)
        else:
            messages.error(request,"Invalid Information")
            return HttpResponseRedirect('/contact/')
    else:
        form = Form()
    return render(request,'app/Contact.html',{'form':form})