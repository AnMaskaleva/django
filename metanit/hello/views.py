from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

def index(requst):
    bob = Person("Bob", 41)
    return JsonResponse(bob, safe=False, encoder=PersonEncorder)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonEncorder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
        return super().default(obj)