
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("lists/", include("lists.urls"))
]
