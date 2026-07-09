from django.urls import path
from . import views

urlpatterns = [

    path("", views.course_list, name="course_list"),

    path("add/", views.course_add, name="course_add"),

    path("profile/<int:id>/",
         views.course_profile,
         name="course_profile"),

    path("update/<int:id>/",
         views.course_update,
         name="course_update"),

    path("delete/<int:id>/",
         views.course_delete,
         name="course_delete"),

]