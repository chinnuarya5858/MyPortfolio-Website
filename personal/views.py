from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def education(request):
    return render(request,'education.html')

def skills(request):
    return render(request,'skills.html')

def certificates(request):
    return render(request,'awards.html')

def contact(request):
    form=ContactForm()
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                subject='New Contact Form Submission',
                message="Thank you for reaching out.We'll get back to you shortly",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['aryakunjumon21@gmail.com'],
                fail_silently=False,
            )
            messages.success(request,'Thanks for reaching out')
            return redirect('contact')
    return render(request,'contact.html',{'form':form})

def base(request):
    return render(request,'homepage.html')