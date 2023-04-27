from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("teachers-create/", views.teacher_display, name="teacher_display"),
]
