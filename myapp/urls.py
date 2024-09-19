from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("getform/", views.getform, name='getform'),
    path("showform/", views.showform, name='showform'),
]
