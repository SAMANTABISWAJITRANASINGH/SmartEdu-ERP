from django.contrib import admin
from .models import Examination


@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):

    list_display = (
        "exam_id",
        "student",
        "subject",
        "department",
        "course",
        "exam_date",
        "obtained_marks",
        "total_marks",
        "grade",
        "result",
    )

    search_fields = (
        "student__first_name",
        "student__last_name",
        "subject",
        "department",
    )

    list_filter = (
        "department",
        "course",
        "result",
        "grade",
        "exam_date",
    )