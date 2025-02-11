from django.shortcuts import render

def index(request):
    data = {"n":5}
    return render(request, "index.html", context = data)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

class Person:

    def __init__(self, name):
        self.name = name