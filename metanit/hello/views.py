from django.template.response import TemplateResponse

def index(request):
    header = "Данные пользователя" #переменная
    langs = ["Python", "Java", "C#"] #список
    user = {"name":"Tom", "age":23} #словарь
    address = ("Абрикосовая", 23, 45) #кортеж

    data = {"header":header, "langs":langs, "user":user, "address":address}
    return TemplateResponse(request, "index.html", data)

def about(request):
    return TemplateResponse(request, "about.html")

def contact(request):
    return TemplateResponse(request, "contact.html")