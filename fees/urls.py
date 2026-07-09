from django.urls import path
from . import views

urlpatterns = [

    path("", views.fee_list, name="fee_list"),

    path("add/", views.fee_add, name="fee_add"),

    path("profile/<int:id>/",
         views.fee_profile,
         name="fee_profile"),

    path("update/<int:id>/",
         views.fee_update,
         name="fee_update"),

    path("delete/<int:id>/",
         views.fee_delete,
         name="fee_delete"),

    path("receipt/<int:id>/",
         views.fee_receipt,
         name="fee_receipt"),

]