from django.contrib import admin
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):

    list_display = (
        "notice_id",
        "title",
        "category",
        "notice_date",
        "expiry_date",
        "status",
    )

    search_fields = (
        "title",
        "category",
    )

    list_filter = (
        "status",
        "category",
        "notice_date",
    )