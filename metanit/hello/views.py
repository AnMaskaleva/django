from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, "index.html")

def about(request):
    return TemplateResponse(request, "about.html")

def contact(request):
    return TemplateResponse(request, "contact.html")