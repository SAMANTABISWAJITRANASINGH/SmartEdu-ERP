from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Student
import re


# =====================================================
# STUDENT LIST + NORMAL SEARCH + VOICE COMMANDS
# =====================================================
def student_list(request):

    search = request.GET.get("search", "").strip()

    students = Student.objects.all()

    voice_message = ""

    if search:

        original_command = search.strip()
        command = original_command.lower().strip()

        # -------------------------------------------------
        # COMMAND: SHOW ALL STUDENTS / RESTORE ALL DATA
        # -------------------------------------------------

        show_all_commands = [
            "show all students",
            "show me all students",
            "display all students",
            "restore all students",
            "restore all data",
            "show all data",
            "reset",
            "clear search",
        ]

        if command in show_all_commands:

            students = Student.objects.all()

            voice_message = "Showing all student records."

        else:

            cleaned_name = command

            phrases_to_remove = [
                "show me",
                "show",
                "find me",
                "find",
                "search for",
                "search",
                "open",
                "display",
                "give me",
                "tell me about",
                "student",
                "students",
                "student's",
                "data",
                "details",
                "detail",
                "record",
                "records",
                "profile",
                "information",
                "info",
                "please",
                "of",
            ]

            for phrase in phrases_to_remove:
                cleaned_name = cleaned_name.replace(phrase, " ")

            # Swadhin's -> Swadhin
            cleaned_name = re.sub(
                r"'s\b",
                "",
                cleaned_name
            )

            # Remove punctuation
            cleaned_name = re.sub(
                r"[^\w\s-]",
                " ",
                cleaned_name
            )

            # Remove extra spaces
            cleaned_name = " ".join(
                cleaned_name.split()
            )

            # Search database
            if cleaned_name:

                words = cleaned_name.split()

                query = Q()

                for word in words:
                    query &= (
                        Q(first_name__icontains=word) |
                        Q(last_name__icontains=word) |
                        Q(email__icontains=word) |
                        Q(phone__icontains=word) |
                        Q(course__icontains=word) |
                        Q(department__icontains=word)
                    )
                                    # Gender filter
                if "female" in cleaned_name:
                    query &= Q(gender__iexact="Female")

                elif "male" in cleaned_name:
                    query &= Q(gender__iexact="Male")

                students = Student.objects.filter(query).distinct()

                if students.exists():
                    voice_message = (
                        f"Found {students.count()} student(s)."
                    )
                else:
                    voice_message = (
                        f"No student record found for "
                        f"'{cleaned_name.title()}'."
                    )

    context = {
        "students": students,
        "search_query": search,
        "voice_message": voice_message,
    }

    return render(
        request,
        "students/student_list.html",
        context,
    )


# =====================================================
# ADD STUDENT
# =====================================================
def student_add(request):

    if request.method == "POST":

        student = Student(

            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            gender=request.POST.get("gender"),
            dob=request.POST.get("dob"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            department=request.POST.get("department"),
            course=request.POST.get("course"),
            admission_date=request.POST.get("admission_date"),
        )

        if request.FILES.get("photo"):
            student.photo = request.FILES["photo"]

        student.save()

        return redirect("student_list")

    return render(
        request,
        "students/student_add.html"
    )


# =====================================================
# STUDENT PROFILE
# =====================================================
def student_profile(request, id):

    student = get_object_or_404(
        Student,
        student_id=id
    )

    return render(
        request,
        "students/student_profile.html",
        {
            "student": student
        }
    )


# =====================================================
# UPDATE STUDENT
# =====================================================
def student_update(request, id):

    student = get_object_or_404(
        Student,
        student_id=id
    )

    if request.method == "POST":

        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.gender = request.POST.get("gender")
        student.dob = request.POST.get("dob")
        student.email = request.POST.get("email")
        student.phone = request.POST.get("phone")
        student.address = request.POST.get("address")
        student.department = request.POST.get("department")
        student.course = request.POST.get("course")
        student.admission_date = request.POST.get("admission_date")

        if request.FILES.get("photo"):
            student.photo = request.FILES["photo"]

        student.save()

        return redirect("student_list")

    return render(
        request,
        "students/student_update.html",
        {
            "student": student
        }
    )


# =====================================================
# DELETE STUDENT
# =====================================================
def student_delete(request, id):

    student = get_object_or_404(
        Student,
        student_id=id
    )

    if request.method == "POST":

        student.delete()

        return redirect("student_list")

    return render(
        request,
        "students/student_delete.html",
        {
            "student": student
        }
    )


# =====================================================
# STUDENT DASHBOARD
# =====================================================
@login_required
def student_dashboard(request):

    return render(
        request,
        "students/student_dashboard.html"
    )