from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import BookingObject, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

def object_list(request):
    """
    Отображает список доступных объектов.
    """

    objects = BookingObject.objects.filter(
        is_available=True
    )

    return render(
        request,
        "reservations/object_list.html",
        {
            "objects": objects
        }
    )


def object_detail(request, pk):
    """
    Отображает подробную информацию об объекте.
    """

    booking_object = get_object_or_404(
        BookingObject,
        id=pk
    )

    return render(
        request,
        "reservations/object_detail.html",
        {
            "object": booking_object
        }
    )


@login_required
def create_booking(request, pk):
    """
    Создание нового бронирования с проверкой конфликтов.
    """

    booking_object = get_object_or_404(
        BookingObject,
        id=pk
    )

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user
            booking.booking_object = booking_object

            conflict = Booking.objects.filter(
                booking_object=booking_object,
                start_time__lt=booking.end_time,
                end_time__gt=booking.start_time,
                status='active'
            ).exists()

            if conflict:
                messages.error(
                    request,
                    " Это время уже занято"
                )
            else:
                booking.save()
                messages.success(
                    request,
                    " Бронирование успешно создано"
                )
                return redirect("profile")

    else:
        form = BookingForm()

    return render(
        request,
        "reservations/create_booking.html",
        {
            "form": form,
            "object": booking_object,
        }
    )
    
@login_required
def create_booking(request, pk):
    ...