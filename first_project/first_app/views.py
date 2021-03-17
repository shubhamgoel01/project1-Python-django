from django.shortcuts import render
from datetime import datetime
from first_app.models import Contact
from django.contrib import messages
from os import getenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


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

        # Saving to database
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()

        # Sending mail
        message = Mail(
            from_email=str(getenv("SENDGRID_EMAIL_ID")),
            to_emails="tapajkumardas@gmail.com",
            subject="New contact request",
            html_content='<strong>' + name + '<br>' + phone + '<br>' + email + '<br>' + desc + '<strong>')
        try:
            sg = SendGridAPIClient(getenv("SENDGRID_API_KEY"))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
