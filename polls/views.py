from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker

from .models import Teacher

fake = Faker()
res, resalt = [], []


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html")


def teacher_display(request, count=100):
    # data = serializers.serialize("python", Teacher.objects.all())
    # for i in data:
    for i in Teacher.objects.all():
        resalt.append(i)

    if request.method == 'GET' and request.GET.get('count') is not None:
        count = request.GET.get('count')

        try:
            count = int(count)
            if 1 > count or count > 100:
                raise ValueError("Invalid count value! Please, input students count as integer between 1 and 100")
        except ValueError as error:
            return HttpResponse(f"Invalid count parameter: {str(error)}")

        for i in range(count):
            teacher = Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=fake.random_int(min=18, max=50),
                email=fake.email(),

            )

            col_last = f"{teacher.id}: {teacher.first_name} {teacher.last_name} ({teacher.age} years old) - {teacher.email}"
            res.append(col_last)

        return render(request, "teachers.html", context={"res": f"{res}", "res0": f"{resalt}"})
    else:

        for i in range(count):
            teacher = Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=fake.random_int(min=18, max=50),
                email=fake.email(),

            )

            col = f"{teacher.id}: {teacher.first_name} {teacher.last_name} ({teacher.age} years old) - {teacher.email}"
            res.append(col)

        return render(request, "teachers.html", context={"res": f"{res}"})
