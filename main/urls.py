from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #home page
    path("v1/", views.v1, name="view 1"), #version 1 of the view
]
