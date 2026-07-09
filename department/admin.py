from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        "department_id",
        "department_name",
        "department_code",
        "hod",
        "email",
        "phone",
        "total_teachers",
        "total_students",
    )

    search_fields = (
        "department_name",
        "department_code",
        "hod",
    )

    list_filter = (
        "department_name",
    )