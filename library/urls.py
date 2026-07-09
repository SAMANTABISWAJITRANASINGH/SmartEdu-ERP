from django.urls import path
from . import views

urlpatterns = [

    path("", views.book_list, name="book_list"),

    path("add/", views.book_add, name="book_add"),

    path("profile/<int:id>/",
         views.book_profile,
         name="book_profile"),

    path("update/<int:id>/",
         views.book_update,
         name="book_update"),

    path("delete/<int:id>/",
         views.book_delete,
         name="book_delete"),

    path("issue/",
         views.issue_book,
         name="issue_book"),

    path("return/",
         views.return_book,
         name="return_book"),

    path("report/",
         views.library_report,
         name="library_report"),

]