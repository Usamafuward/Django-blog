
from django.contrib import admin
from django.urls import path, include

handler404 = 'myproject.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls"))
]
