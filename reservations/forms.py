from django import forms

from .models import Booking


class BookingForm(forms.ModelForm):
    """Форма создания бронирования."""


    class Meta:
        """Настройки формы."""

        model = Booking

        fields = [
            "start_datetime",
            "end_datetime",
        ]


        widgets = {

            "start_datetime": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control"
                }
            ),


            "end_datetime": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control"
                }
            ),

        }