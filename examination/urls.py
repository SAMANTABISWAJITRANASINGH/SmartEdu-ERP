from django.urls import path
from . import views

urlpatterns = [

    path("", views.examination_list, name="examination_list"),

    path("add/", views.examination_add, name="examination_add"),

    path("profile/<int:id>/",
         views.examination_profile,
         name="examination_profile"),

    path("update/<int:id>/",
         views.examination_update,
         name="examination_update"),

    path("delete/<int:id>/",
         views.examination_delete,
         name="examination_delete"),

    path("result/<int:id>/",
         views.examination_result,
         name="examination_result"),
]