from django.urls import path
from . import views

urlpatterns = [

    path("", views.notice_list, name="notice_list"),

    path("add/", views.notice_add, name="notice_add"),

    path("profile/<int:id>/",
         views.notice_profile,
         name="notice_profile"),

    path("update/<int:id>/",
         views.notice_update,
         name="notice_update"),

    path("delete/<int:id>/",
         views.notice_delete,
         name="notice_delete"),

]