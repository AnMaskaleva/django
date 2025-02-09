from django.urls import path, include
from hello import views

product_patterns = [
    path("", views.products),
    path("comments", views.comments),
    path("questions", views.questions),
]

urlpatterns = [
    path("", views.index),
    path("user/", views.user)
]