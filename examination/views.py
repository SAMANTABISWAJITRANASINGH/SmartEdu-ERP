from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Examination
from students.models import Student


# -----------------------------
# Examination List
# -----------------------------
def examination_list(request):

    search = request.GET.get("search")

    if search:
        examinations = Examination.objects.filter(
            Q(student__first_name__icontains=search) |
            Q(student__last_name__icontains=search) |
            Q(subject__icontains=search) |
            Q(course__icontains=search) |
            Q(department__icontains=search)
        )
    else:
        examinations = Examination.objects.all()

    return render(
        request,
        "examination/examination_list.html",
        {"examinations": examinations}
    )


# -----------------------------
# Add Examination
# -----------------------------
def examination_add(request):

    students = Student.objects.all()

    if request.method == "POST":

        student = get_object_or_404(
            Student,
            student_id=request.POST.get("student")
        )

        Examination.objects.create(

            student=student,

            department=request.POST.get("department"),

            course=request.POST.get("course"),

            subject=request.POST.get("subject"),

            exam_date=request.POST.get("exam_date"),

            total_marks=request.POST.get("total_marks"),

            obtained_marks=request.POST.get("obtained_marks"),

            grade=request.POST.get("grade"),

            result=request.POST.get("result"),

            remarks=request.POST.get("remarks"),

        )

        return redirect("examination_list")

    return render(
        request,
        "examination/examination_add.html",
        {"students": students}
    )


# -----------------------------
# Examination Profile
# -----------------------------
def examination_profile(request, id):

    examination = get_object_or_404(
        Examination,
        exam_id=id
    )

    return render(
        request,
        "examination/examination_profile.html",
        {"examination": examination}
    )


# -----------------------------
# Update Examination
# -----------------------------
def examination_update(request, id):

    examination = get_object_or_404(
        Examination,
        exam_id=id
    )

    students = Student.objects.all()

    if request.method == "POST":

        examination.student = get_object_or_404(
            Student,
            student_id=request.POST.get("student")
        )

        examination.department = request.POST.get("department")
        examination.course = request.POST.get("course")
        examination.subject = request.POST.get("subject")
        examination.exam_date = request.POST.get("exam_date")
        examination.total_marks = request.POST.get("total_marks")
        examination.obtained_marks = request.POST.get("obtained_marks")
        examination.grade = request.POST.get("grade")
        examination.result = request.POST.get("result")
        examination.remarks = request.POST.get("remarks")

        examination.save()

        return redirect("examination_list")

    return render(
        request,
        "examination/examination_update.html",
        {
            "examination": examination,
            "students": students,
        }
    )


# -----------------------------
# Delete Examination
# -----------------------------
def examination_delete(request, id):

    examination = get_object_or_404(
        Examination,
        exam_id=id
    )

    if request.method == "POST":

        examination.delete()

        return redirect("examination_list")

    return render(
        request,
        "examination/examination_delete.html",
        {"examination": examination}
    )


# -----------------------------
# Examination Result
# -----------------------------
def examination_result(request, id):

    examination = get_object_or_404(
        Examination,
        exam_id=id
    )

    return render(
        request,
        "examination/examination_result.html",
        {"examination": examination}
    )