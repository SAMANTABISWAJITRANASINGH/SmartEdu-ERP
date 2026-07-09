

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Teacher


# -----------------------------
# Teacher List + Search
# -----------------------------
def teacher_list(request):

    search = request.GET.get("search")

    if search:
        teachers = Teacher.objects.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search) |
            Q(phone__icontains=search) |
            Q(department__icontains=search) |
            Q(qualification__icontains=search)
        )
    else:
        teachers = Teacher.objects.all()

    return render(
        request,
        "teachers/teacher_list.html",
        {"teachers": teachers}
    )


# -----------------------------
# Add Teacher
# -----------------------------
def teacher_add(request):

    if request.method == "POST":

        teacher = Teacher(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            gender=request.POST.get("gender"),
            dob=request.POST.get("dob"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            qualification=request.POST.get("qualification"),
            department=request.POST.get("department"),
            joining_date=request.POST.get("joining_date"),
            salary=request.POST.get("salary"),
        )

        if request.FILES.get("photo"):
            teacher.photo = request.FILES["photo"]

        teacher.save()

        return redirect("teacher_list")

    return render(request, "teachers/teacher_add.html")


# -----------------------------
# Teacher Profile
# -----------------------------
def teacher_profile(request, id):

    teacher = get_object_or_404(
        Teacher,
        teacher_id=id
    )

    return render(
        request,
        "teachers/teacher_profile.html",
        {"teacher": teacher}
    )


# -----------------------------
# Update Teacher
# -----------------------------
def teacher_update(request, id):

    teacher = get_object_or_404(
        Teacher,
        teacher_id=id
    )

    if request.method == "POST":

        teacher.first_name = request.POST.get("first_name")
        teacher.last_name = request.POST.get("last_name")
        teacher.gender = request.POST.get("gender")
        teacher.dob = request.POST.get("dob")
        teacher.email = request.POST.get("email")
        teacher.phone = request.POST.get("phone")
        teacher.address = request.POST.get("address")
        teacher.qualification = request.POST.get("qualification")
        teacher.department = request.POST.get("department")
        teacher.joining_date = request.POST.get("joining_date")
        teacher.salary = request.POST.get("salary")

        if request.FILES.get("photo"):
            teacher.photo = request.FILES["photo"]

        teacher.save()

        return redirect("teacher_list")

    return render(
        request,
        "teachers/teacher_update.html",
        {"teacher": teacher}
    )


# -----------------------------
# Delete Teacher
# -----------------------------
def teacher_delete(request, id):

    teacher = get_object_or_404(
        Teacher,
        teacher_id=id
    )

    if request.method == "POST":

        teacher.delete()

        return redirect("teacher_list")

    return render(
        request,
        "teachers/teacher_delete.html",
        {"teacher": teacher}
    )
from django.contrib.auth.decorators import login_required

@login_required
def teacher_dashboard(request):
    return render(request, "teachers/teacher_dashboard.html")