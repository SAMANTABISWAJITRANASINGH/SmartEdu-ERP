from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Department


# -----------------------------
# Department List + Search
# -----------------------------
def department_list(request):

    search = request.GET.get("search")

    if search:
        departments = Department.objects.filter(
            Q(department_name__icontains=search) |
            Q(department_code__icontains=search) |
            Q(hod__icontains=search)
        )
    else:
        departments = Department.objects.all()

    return render(
        request,
        "department/department_list.html",
        {"departments": departments}
    )


# -----------------------------
# Add Department
# -----------------------------
def department_add(request):

    if request.method == "POST":

        department = Department(
            department_name=request.POST.get("department_name"),
            department_code=request.POST.get("department_code"),
            hod=request.POST.get("hod"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            location=request.POST.get("location"),
            total_teachers=request.POST.get("total_teachers"),
            total_students=request.POST.get("total_students"),
            description=request.POST.get("description"),
        )

        if request.FILES.get("photo"):
            department.photo = request.FILES["photo"]

        department.save()

        return redirect("department_list")

    return render(request, "department/department_add.html")


# -----------------------------
# Department Profile
# -----------------------------
def department_profile(request, id):

    department = get_object_or_404(
        Department,
        department_id=id
    )

    return render(
        request,
        "department/department_profile.html",
        {"department": department}
    )


# -----------------------------
# Update Department
# -----------------------------
def department_update(request, id):

    department = get_object_or_404(
        Department,
        department_id=id
    )

    if request.method == "POST":

        department.department_name = request.POST.get("department_name")
        department.department_code = request.POST.get("department_code")
        department.hod = request.POST.get("hod")
        department.email = request.POST.get("email")
        department.phone = request.POST.get("phone")
        department.location = request.POST.get("location")
        department.total_teachers = request.POST.get("total_teachers")
        department.total_students = request.POST.get("total_students")
        department.description = request.POST.get("description")

        if request.FILES.get("photo"):
            department.photo = request.FILES["photo"]

        department.save()

        return redirect("department_list")

    return render(
        request,
        "department/department_update.html",
        {"department": department}
    )


# -----------------------------
# Delete Department
# -----------------------------
def department_delete(request, id):

    department = get_object_or_404(
        Department,
        department_id=id
    )

    if request.method == "POST":

        department.delete()

        return redirect("department_list")

    return render(
        request,
        "department/department_delete.html",
        {"department": department}
    )