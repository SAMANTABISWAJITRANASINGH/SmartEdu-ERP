from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Fee
from students.models import Student


# -----------------------------
# Fee List
# -----------------------------
def fee_list(request):

    search = request.GET.get("search")

    if search:
        fees = Fee.objects.filter(
            Q(student__first_name__icontains=search) |
            Q(student__last_name__icontains=search) |
            Q(department__icontains=search) |
            Q(course__icontains=search) |
            Q(fee_type__icontains=search)
        )
    else:
        fees = Fee.objects.all()

    return render(
        request,
        "fees/fee_list.html",
        {"fees": fees}
    )


# -----------------------------
# Add Fee
# -----------------------------
def fee_add(request):

    students = Student.objects.all()

    if request.method == "POST":

        student = get_object_or_404(
            Student,
            student_id=request.POST.get("student")
        )

        Fee.objects.create(

            student=student,

            department=request.POST.get("department"),

            course=request.POST.get("course"),

            fee_type=request.POST.get("fee_type"),

            total_amount=request.POST.get("total_amount"),

            paid_amount=request.POST.get("paid_amount"),

            payment_date=request.POST.get("payment_date"),

            payment_method=request.POST.get("payment_method"),

            status=request.POST.get("status"),

            remarks=request.POST.get("remarks"),

        )

        return redirect("fee_list")

    return render(
        request,
        "fees/fee_add.html",
        {"students": students}
    )


# -----------------------------
# Fee Profile
# -----------------------------
def fee_profile(request, id):

    fee = get_object_or_404(
        Fee,
        fee_id=id
    )

    return render(
        request,
        "fees/fee_profile.html",
        {"fee": fee}
    )


# -----------------------------
# Update Fee
# -----------------------------
def fee_update(request, id):

    fee = get_object_or_404(
        Fee,
        fee_id=id
    )

    students = Student.objects.all()

    if request.method == "POST":

        fee.student = get_object_or_404(
            Student,
            student_id=request.POST.get("student")
        )

        fee.department = request.POST.get("department")
        fee.course = request.POST.get("course")
        fee.fee_type = request.POST.get("fee_type")
        fee.total_amount = request.POST.get("total_amount")
        fee.paid_amount = request.POST.get("paid_amount")
        fee.payment_date = request.POST.get("payment_date")
        fee.payment_method = request.POST.get("payment_method")
        fee.status = request.POST.get("status")
        fee.remarks = request.POST.get("remarks")

        fee.save()

        return redirect("fee_list")

    return render(
        request,
        "fees/fee_update.html",
        {
            "fee": fee,
            "students": students,
        }
    )


# -----------------------------
# Delete Fee
# -----------------------------
def fee_delete(request, id):

    fee = get_object_or_404(
        Fee,
        fee_id=id
    )

    if request.method == "POST":

        fee.delete()

        return redirect("fee_list")

    return render(
        request,
        "fees/fee_delete.html",
        {"fee": fee}
    )


# -----------------------------
# Fee Receipt
# -----------------------------
def fee_receipt(request, id):

    fee = get_object_or_404(
        Fee,
        fee_id=id
    )

    return render(
        request,
        "fees/fee_receipt.html",
        {"fee": fee}
    )