from django.http import JsonResponse

def index(requst):
    return JsonResponse({"name":"Tom", "age":"38"})