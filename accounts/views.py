from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import RegisterForm


def register_view(request):
    """Регистрация нового пользователя."""

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(
                commit=False
            )

            user.set_password(
                form.cleaned_data["password"]
            )

            user.save()

            login(request, user)

            return redirect("/")

    else:

        form = RegisterForm()


    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )

from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from reservations.models import Booking

def login_view(request):
    """Авторизация пользователя."""

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(
                request,
                user
            )

            return redirect("/")


    return render(
        request,
        "accounts/login.html"
    )



def logout_view(request):
    """Выход пользователя из аккаунта."""

    logout(request)

    return redirect("/")



@login_required
def profile_view(request):
    """Личный кабинет пользователя."""

    bookings = Booking.objects.filter(
        user=request.user
    )


    return render(
        request,
        "accounts/profile.html",
        {
            "bookings": bookings
        }
    )