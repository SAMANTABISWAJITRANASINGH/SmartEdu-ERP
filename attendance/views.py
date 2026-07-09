from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Attendance
from students.models import Student


# -----------------------------
# Attendance List
# -----------------------------
def attendance_list(request):

    search = request.GET.get("search")

    if search:
        attendances = Attendance.objects.filter(
            Q(student__first_name__icontains=search) |
            Q(student__last_name__icontains=search) |
            Q(department__icontains=search) |
            Q(course__icontains=search)
        )
    else:
        attendances = Attendance.objects.all()

    return render(
        request,
        "attendance/attendance_list.html",
        {"attendances": attendances}
    )


# -----------------------------
# Add Attendance
# -----------------------------
def attendance_add(request):

    students = Student.objects.all()

    if request.method == "POST":

        student = get_object_or_404(
            Student,
            student_id=request.POST.get("student")
        )

        Attendance.objects.create(
            student=student,
            department=request.POST.get("department"),
            course=request.POST.get("course"),
            attendance_date=request.POST.get("attendance_date"),
            status=request.POST.get("status"),
            remarks=request.POST.get("remarks"),
        )

        return redirect("attendance_list")

    return render(
        request,
        "attendance/attendance_add.html",
        {"students": students}
    )


# -----------------------------
# Attendance Update
# -----------------------------
def attendance_update(request, id):

    attendance = get_object_or_404(
        Attendance,
        attendance_id=id
    )

    students = Student.objects.all()

    if request.method == "POST":

        attendance.student = get_object_or_404(
            Student,
            student_id=request.POST.get("student")
        )

        attendance.department = request.POST.get("department")
        attendance.course = request.POST.get("course")
        attendance.attendance_date = request.POST.get("attendance_date")
        attendance.status = request.POST.get("status")
        attendance.remarks = request.POST.get("remarks")

        attendance.save()

        return redirect("attendance_list")

    return render(
        request,
        "attendance/attendance_update.html",
        {
            "attendance": attendance,
            "students": students,
        }
    )


# -----------------------------
# Attendance Delete
# -----------------------------
def attendance_delete(request, id):

    attendance = get_object_or_404(
        Attendance,
        attendance_id=id
    )

    if request.method == "POST":

        attendance.delete()

        return redirect("attendance_list")

    return render(
        request,
        "attendance/attendance_delete.html",
        {"attendance": attendance}
    )


# -----------------------------
# Attendance Report
# -----------------------------
def attendance_report(request):

    attendances = Attendance.objects.all()

    present_count = Attendance.objects.filter(
        status="Present"
    ).count()

    absent_count = Attendance.objects.filter(
        status="Absent"
    ).count()

    leave_count = Attendance.objects.filter(
        status="Leave"
    ).count()

    return render(
        request,
        "attendance/attendance_report.html",
        {
            "attendances": attendances,
            "present_count": present_count,
            "absent_count": absent_count,
            "leave_count": leave_count,
        }
    )