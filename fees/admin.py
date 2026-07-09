from django.contrib import admin
from .models import Fee


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):

    list_display = (
        "fee_id",
        "student",
        "fee_type",
        "department",
        "course",
        "total_amount",
        "paid_amount",
        "status",
        "payment_date",
    )

    search_fields = (
        "student__first_name",
        "student__last_name",
        "department",
        "course",
        "fee_type",
    )

    list_filter = (
        "status",
        "payment_method",
        "department",
        "payment_date",
    )