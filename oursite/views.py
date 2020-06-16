from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact_us
from .forms import contactForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import RequestContext


# Create your views here.

def index(request):
    return render(request,'oursite/index.html',{})

def contact(request):
    if request.method == 'POST':
        contact_form = contactForm(data=request.POST)
        # print(contact_form.errors)
        if contact_form.is_valid():
            firstname = contact_form.cleaned_data['firstname']
            lastname = contact_form.cleaned_data['lastname']
            email = contact_form.cleaned_data['email']
            subject= contact_form.cleaned_data['subject']
            message= contact_form.cleaned_data['message']
            contact_form.save()
              
            first_name = request.POST.get('firstname')
            last_name= request.POST.get('lastname')
            subject_retrieve= request.POST.get('subject')
            message_retrieve= request.POST.get('message')
            message_retrieve= message_retrieve+ '\t'+'from :'+'\t'+first_name +'\t'+ last_name+ '\n'+'with email:'+'\n'+email 
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['amobittechnologiez@gmail.com']
            xxx = send_mail(subject,message_retrieve,email_from,recipient_list,fail_silently=False)
            messages.success(request,"Your message has been submitted")
            
            return render(request, 'oursite/contact-us.html', {})
        else:
            messages.error(request,"Data to be submitted is invalid")
            return render(request,'oursite/contact-us.html',{})

    else:
        return render(request,'oursite/contact-us.html', {})

def register(request):
    return render(request,'oursite/register.html',{})

def about_us(request):
    return render(request,'oursite/about-us.html',{})  

def services(request):
    return render(request,'oursite/services.html',{})    

def products(request):
    return render(request,'oursite/wex.html',{})    