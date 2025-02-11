from django.shortcuts import render

def index(request):
    data = {"red": "красный", "green": "зеленый", "blue":"синий"}
    return render(request, "index.html", context={"data": data})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

class Person:

    def __init__(self, name):
        self.name = name