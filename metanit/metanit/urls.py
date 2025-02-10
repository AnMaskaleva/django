from django.urls import path
from hello import views

urlpatterns = [
    path("set", views.set),
]