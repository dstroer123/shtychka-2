from django.contrib import admin

from .models import BookingObject


@admin.register(BookingObject)
class BookingObjectAdmin(admin.ModelAdmin):
    """Настройка отображения объектов в админке."""

    list_display = (
        "title",
        "price",
        "is_available",
    )

    list_filter = (
        "is_available",
    )

    search_fields = (
        "title",
    )
    
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Настройка бронирований в админке."""


    list_display = (
        "user",
        "booking_object",
        "start_datetime",
        "end_datetime",
    )


    list_filter = (
        "booking_object",
    )


    search_fields = (
        "user__username",
    )