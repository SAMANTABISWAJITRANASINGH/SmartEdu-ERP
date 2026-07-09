from django.shortcuts import render

from students.models import Student
from teachers.models import Teacher
from courses.models import Course
from department.models import Department
from attendance.models import Attendance
from examination.models import Examination
from fees.models import Fee
from library.models import Book
from notice.models import Notice


def dashboard(request):

    context = {

        "total_students": Student.objects.count(),

        "total_teachers": Teacher.objects.count(),

        "total_courses": Course.objects.count(),

        "total_departments": Department.objects.count(),

        "total_attendance": Attendance.objects.count(),

        "total_examinations": Examination.objects.count(),

        "total_fees": Fee.objects.count(),

        "total_books": Book.objects.count(),

        "total_notices": Notice.objects.count(),

        "latest_notices": Notice.objects.order_by("-notice_date")[:5],

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )