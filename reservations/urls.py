from django.urls import path

from .views import (
    object_list,
    object_detail,
    create_booking,
)


urlpatterns = [

    path(
        "objects/",
        object_list,
        name="object_list"
    ),


    path(
        "objects/<int:pk>/",
        object_detail,
        name="object_detail"
    ),
    path(
    "booking/<int:pk>/",
    create_booking,
    name="create_booking"
),
]