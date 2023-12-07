from django.shortcuts import render
from products.models import Contact_us

def index(request):
    return render(request, "index.html")

def contact(request):
    context = {}
    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        email = data.get("email")
        subject = data.get("subject")
        message = data.get("message")

        obj = Contact_us(name=name, email=email, subject=subject, message=message)
        obj.save()
        context["message"] = f"Dear {name}, Your form is submitted successfully!"
    return render(request, "contact.html", context)

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")
def booking(request):
    return render(request, "booking.html")
def feature(request):
    return render(request, "feature.html")
def menu(request):
    return render(request, "menu.html")
def single(request):
    return render(request, "single.html")
def team(request):
    return render(request, "team.html")

