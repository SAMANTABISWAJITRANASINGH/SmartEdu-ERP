# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Teacher
import re


# -----------------------------
# Teacher List + Search+ voice 
# -----------------------------
def teacher_list(request):

    search = request.GET.get("search", "").strip()

    teachers = Teacher.objects.all()

    voice_message = ""

    if search:

        command = search.lower().strip()

        show_all_commands = [
            "show all teachers",
            "show me all teachers",
            "display all teachers",
            "show all data",
            "restore all teachers",
            "reset",
            "clear search",
        ]

        if command in show_all_commands:

            teachers = Teacher.objects.all()
            voice_message = "Showing all teachers."

        else:

            cleaned_name = command

            phrases = [
                "show me",
                "show",
                "find me",
                "find",
                "search",
                "search for",
                "teacher",
                "teachers",
                "teacher's",
                "data",
                "details",
                "detail",
                "record",
                "records",
                "profile",
                "information",
                "info",
                "please",
            ]

            for phrase in phrases:
                cleaned_name = cleaned_name.replace(phrase, " ")

            cleaned_name = re.sub(r"'s\b", "", cleaned_name)
            cleaned_name = re.sub(r"[^\w\s-]", " ", cleaned_name)
            cleaned_name = " ".join(cleaned_name.split())

            if cleaned_name:

                words = cleaned_name.split()

                query = Q()

                for word in words:
                    query &= (
                        Q(first_name__icontains=word) |
                        Q(last_name__icontains=word) |
                        Q(email__icontains=word) |
                        Q(phone__icontains=word) |
                        Q(department__icontains=word) |
                        Q(qualification__icontains=word)
                    )

                if "male" in cleaned_name:
                    query &= Q(gender__iexact="Male")

                elif "female" in cleaned_name:
                    query &= Q(gender__iexact="Female")

                teachers = Teacher.objects.filter(query).distinct()

                if teachers.exists():
                    voice_message = f"Found {teachers.count()} teacher(s)."
                else:
                    voice_message = "No teacher found."

    context = {
        "teachers": teachers,
        "search_query": search,
        "voice_message": voice_message,
    }

    return render(
        request,
        "teachers/teacher_list.html",
        context,
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