from django.shortcuts import render

def index(request):
    langs = ["Python", "JavaScript", "Java", "C#", "C++"]
    return render(request, "index.html", context={"langs": langs})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

class Person:

    def __init__(self, name):
        self.name = name