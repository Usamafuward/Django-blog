from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:slug>", views.detail, name="detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]