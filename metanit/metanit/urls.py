from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("about/", TemplateView.as_view(template_name="about.html",
        extra_context={"header":"О сайте"})),
    path("contact/", TemplateView.as_view(template_name="contact.html")),
]