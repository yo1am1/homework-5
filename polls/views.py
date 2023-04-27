from django.shortcuts import render

from .models import Teacher


def index(request):
    return render(request, "index.html")


def teacher_display(request):
    res_alt = list(Teacher.objects.values())
    return render(request, "teachers.html", context={"res0": f"{res_alt}"})
