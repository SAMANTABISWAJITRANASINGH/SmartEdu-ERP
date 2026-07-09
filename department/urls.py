from django.urls import path
from . import views

urlpatterns = [

    path("", views.department_list, name="department_list"),

    path("add/", views.department_add, name="department_add"),

    path("profile/<int:id>/",
         views.department_profile,
         name="department_profile"),

    path("update/<int:id>/",
         views.department_update,
         name="department_update"),

    path("delete/<int:id>/",
         views.department_delete,
         name="department_delete"),

]