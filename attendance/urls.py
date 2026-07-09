from django.urls import path
from . import views

urlpatterns = [

    path("", views.attendance_list, name="attendance_list"),

    path("add/", views.attendance_add, name="attendance_add"),

    path("update/<int:id>/",
         views.attendance_update,
         name="attendance_update"),

    path("delete/<int:id>/",
         views.attendance_delete,
         name="attendance_delete"),

    path("report/",
         views.attendance_report,
         name="attendance_report"),
]