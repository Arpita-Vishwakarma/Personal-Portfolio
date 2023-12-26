from django.shortcuts import render, HttpResponse
from django import template
from django.template import loader
from django.core.mail import send_mail
from .forms import UserInfoForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.
def index(request):
    form = UserInfoForm(request.POST)
    if request.method == 'POST':
        print("Working..")
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name)
            
            # Sending email with form data
            subject = 'New Form Submission'
            message_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            sender_email = email  # Replace with your email address
            recipient_list = ['VishwakarmaArpita1219@gmail.com']  # Replace with recipient's email address

            send_mail(subject, message_body, sender_email, recipient_list, fail_silently=False)

            messages.success(request, 'Email sent successfully!')
            return render(request, 'index.html')  # Redirect to a success page
        else:
            messages.error(request, 'Something went wrong! Please check the form.')
    else:
        form = UserInfoForm()
    
    return render(request, 'index.html', {'form': form})