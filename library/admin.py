from django.contrib import admin
from .models import Book, BookIssue


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "book_id",
        "title",
        "author",
        "category",
        "publisher",
        "available_copies",
    )

    search_fields = (
        "title",
        "author",
        "isbn",
    )

    list_filter = (
        "category",
        "publisher",
    )


@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):

    list_display = (
        "issue_id",
        "student",
        "book",
        "issue_date",
        "return_date",
        "status",
        "fine",
    )

    search_fields = (
        "student__first_name",
        "book__title",
    )

    list_filter = (
        "status",
        "issue_date",
    )