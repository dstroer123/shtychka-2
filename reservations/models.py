from django.db import models


class BookingObject(models.Model):
    """Модель объекта, доступного для бронирования."""

    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    image = models.ImageField(
        upload_to="objects/",
        verbose_name="Фото"
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Цена за час"
    )

    is_available = models.BooleanField(
        default=True,
        verbose_name="Доступен"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        """Настройки отображения модели."""

        verbose_name = "Объект бронирования"
        verbose_name_plural = "Объекты бронирования"


    def __str__(self):
        """Возвращает название объекта."""

        return self.title
    
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Booking(models.Model):
    """Модель бронирования объекта."""


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )


    booking_object = models.ForeignKey(
        BookingObject,
        on_delete=models.CASCADE,
        verbose_name="Объект"
    )


    start_datetime = models.DateTimeField(
        verbose_name="Начало бронирования"
    )


    end_datetime = models.DateTimeField(
        verbose_name="Конец бронирования"
    )


    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создано"
    )


    class Meta:
        """Настройки модели."""

        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"


    def clean(self):
        """Проверка пересечения времени."""

        conflicts = Booking.objects.filter(
            booking_object=self.booking_object,
            start_datetime__lt=self.end_datetime,
            end_datetime__gt=self.start_datetime,
        ).exclude(
            id=self.id
        )


        if conflicts.exists():

            raise ValidationError(
                "Этот объект уже забронирован в выбранное время."
            )


    def __str__(self):
        """Отображение бронирования."""

        return (
            f"{self.user} - "
            f"{self.booking_object}"
        )