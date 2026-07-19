from django.shortcuts import render

from .models import BookingObject
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import BookingForm
from .models import BookingObject, Booking


def object_list(request):
    """Отображает список доступных объектов."""

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
    """Отображает подробную информацию об объекте."""

    booking_object = BookingObject.objects.get(
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
    """Создание нового бронирования."""

    booking_object = get_object_or_404(
        BookingObject,
        id=pk
    )


    if request.method == "POST":

        form = BookingForm(
            request.POST
        )


        if form.is_valid():

            booking = form.save(
                commit=False
            )

            booking.user = request.user

            booking.booking_object = (
                booking_object
            )

            booking.save()


            return redirect(
                "profile"
            )


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