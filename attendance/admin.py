from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "attendance_id",
        "student",
        "department",
        "course",
        "attendance_date",
        "status",
    )

    list_filter = (
        "status",
        "department",
        "attendance_date",
    )

    search_fields = (
        "student__first_name",
        "student__last_name",
        "department",
        "course",
    )