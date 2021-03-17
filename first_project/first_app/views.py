from django.shortcuts import render
from datetime import datetime
from first_app.models import Contact
from django.contrib import messages


def index(request):
    context = {
        'variable1': "its me Django Expert!",
        'variable2': "its me Python Expert!",
    }
    return render(request, 'index.html', context)


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
