from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher
from courses.models import Course


def home(request):
    context = {
        "total_students": Student.objects.count(),
        "total_teachers": Teacher.objects.count(),
        "total_courses": Course.objects.count(),
    }

    return render(request, "home/home.html", context)