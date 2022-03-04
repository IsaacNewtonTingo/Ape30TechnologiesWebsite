from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, "formSubmission/index.html")


def contactUs(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        message = request.POST['message']

        # send mail
        send_mail(
            "Form submission at Ape 30 Technologies ",  # subject
            message + "\n" "Name : " + name + "\n" "Phone number : " + \
            phoneNumber + "\n" "Email : " + email,  # message
            email,  # from email
            ['ape30technologies@gmail.com'],  # to email
        )
        return render(request, "formSubmission/contactUs.html", {
            "name": name
        })
    else:
        return render(request, "formSubmission/contactUs.html")


def hireUs(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        message = request.POST['message']

        # send mail
        send_mail(
            "Form submission at Ape 30 Technologies ",  # subject
            message + "\n" "Name : " + name + "\n" "Phone number : " + \
            phoneNumber + "\n" "Email : " + email,  # message
            email,  # from email
            ['ape30technologies@gmail.com'],  # to email
        )
        return render(request, "formSubmission/hireUs.html", {
            "name": name
        })
    else:
        return render(request, "formSubmission/hireUs.html")


def mobileApps(request):
    return render(request, "formSubmission/mobileApps.html")
