from django.shortcuts import render

def index(request):
    data = {"header":"Hello Django", "message":"Welcome to Python"}
    return render(request, "index.html", context=data)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")