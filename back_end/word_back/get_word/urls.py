from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_my_word, name="get_my_word"),
    path("add/", views.add_word, name="add_my_word"),
]