from django.urls import path

from apps.basic.views import basic_module

urlpatterns = [
    path("", basic_module, name="basic_module"),
]
