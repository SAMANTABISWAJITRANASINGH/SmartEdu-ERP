from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Course


# -----------------------------
# Course List + Search
# -----------------------------
def course_list(request):

    search = request.GET.get("search")

    if search:
        courses = Course.objects.filter(
            Q(course_name__icontains=search) |
            Q(course_code__icontains=search) |
            Q(department__icontains=search) |
            Q(coordinator__icontains=search)
        )
    else:
        courses = Course.objects.all()

    return render(
        request,
        "courses/course_list.html",
        {"courses": courses}
    )


# -----------------------------
# Add Course
# -----------------------------
def course_add(request):

    if request.method == "POST":

        course = Course(
            course_name=request.POST.get("course_name"),
            course_code=request.POST.get("course_code"),
            department=request.POST.get("department"),
            duration=request.POST.get("duration"),
            fees=request.POST.get("fees"),
            total_seats=request.POST.get("total_seats"),
            available_seats=request.POST.get("available_seats"),
            coordinator=request.POST.get("coordinator"),
            description=request.POST.get("description"),
        )

        if request.FILES.get("photo"):
            course.photo = request.FILES["photo"]

        course.save()

        return redirect("course_list")

    return render(request, "courses/course_add.html")


# -----------------------------
# Course Profile
# -----------------------------
def course_profile(request, id):

    course = get_object_or_404(
        Course,
        course_id=id
    )

    return render(
        request,
        "courses/course_profile.html",
        {"course": course}
    )


# -----------------------------
# Update Course
# -----------------------------
def course_update(request, id):

    course = get_object_or_404(
        Course,
        course_id=id
    )

    if request.method == "POST":

        course.course_name = request.POST.get("course_name")
        course.course_code = request.POST.get("course_code")
        course.department = request.POST.get("department")
        course.duration = request.POST.get("duration")
        course.fees = request.POST.get("fees")
        course.total_seats = request.POST.get("total_seats")
        course.available_seats = request.POST.get("available_seats")
        course.coordinator = request.POST.get("coordinator")
        course.description = request.POST.get("description")

        if request.FILES.get("photo"):
            course.photo = request.FILES["photo"]

        course.save()

        return redirect("course_list")

    return render(
        request,
        "courses/course_update.html",
        {"course": course}
    )


# -----------------------------
# Delete Course
# -----------------------------
def course_delete(request, id):

    course = get_object_or_404(
        Course,
        course_id=id
    )

    if request.method == "POST":

        course.delete()

        return redirect("course_list")

    return render(
        request,
        "courses/course_delete.html",
        {"course": course}
    )