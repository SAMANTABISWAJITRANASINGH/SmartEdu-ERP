from django.urls import path
from . import views

urlpatterns = [

    path("", views.teacher_list, name="teacher_list"),

    path("add/", views.teacher_add, name="teacher_add"),

    path("profile/<int:id>/",
         views.teacher_profile,
         name="teacher_profile"),

    path("update/<int:id>/",
         views.teacher_update,
         name="teacher_update"),

    path("delete/<int:id>/",
         views.teacher_delete,
         name="teacher_delete"),
         path(
    "dashboard/",
    views.teacher_dashboard,
    name="teacher_dashboard"
),
]