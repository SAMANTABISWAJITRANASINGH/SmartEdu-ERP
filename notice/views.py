from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Notice


# ===============================
# Notice List
# ===============================

def notice_list(request):

    search = request.GET.get("search")

    if search:

        notices = Notice.objects.filter(

            Q(title__icontains=search) |
            Q(category__icontains=search) |
            Q(description__icontains=search)

        )

    else:

        notices = Notice.objects.all()

    return render(

        request,

        "notice/notice_list.html",

        {

            "notices": notices

        }

    )


# ===============================
# Add Notice
# ===============================

def notice_add(request):

    if request.method == "POST":

        Notice.objects.create(

            title=request.POST.get("title"),

            category=request.POST.get("category"),

            description=request.POST.get("description"),

            notice_date=request.POST.get("notice_date"),

            expiry_date=request.POST.get("expiry_date"),

            attachment=request.FILES.get("attachment"),

            status=request.POST.get("status"),

        )

        return redirect("notice_list")

    return render(

        request,

        "notice/notice_add.html"

    )


# ===============================
# Notice Profile
# ===============================

def notice_profile(request, id):

    notice = get_object_or_404(

        Notice,

        notice_id=id

    )

    return render(

        request,

        "notice/notice_profile.html",

        {

            "notice": notice

        }

    )


# ===============================
# Update Notice
# ===============================

def notice_update(request, id):

    notice = get_object_or_404(

        Notice,

        notice_id=id

    )

    if request.method == "POST":

        notice.title = request.POST.get("title")

        notice.category = request.POST.get("category")

        notice.description = request.POST.get("description")

        notice.notice_date = request.POST.get("notice_date")

        notice.expiry_date = request.POST.get("expiry_date")

        notice.status = request.POST.get("status")

        if request.FILES.get("attachment"):

            notice.attachment = request.FILES.get("attachment")

        notice.save()

        return redirect("notice_list")

    return render(

        request,

        "notice/notice_update.html",

        {

            "notice": notice

        }

    )


# ===============================
# Delete Notice
# ===============================

def notice_delete(request, id):

    notice = get_object_or_404(

        Notice,

        notice_id=id

    )

    if request.method == "POST":

        notice.delete()

        return redirect("notice_list")

    return render(

        request,

        "notice/notice_delete.html",

        {

            "notice": notice

        }

    )