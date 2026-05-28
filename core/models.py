from django.db import models
from django.contrib.postgres.fields import ArrayField, DateTimeRangeField


class RoomReservation(models.Model):
    room_name = models.CharField(max_length=100, verbose_name='Название зала')

    # Расширенное поле: Массив строк (сохраняет элементы списка Python)
    amenities = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        null=True,
        verbose_name='Необходимое оборудование (список)'
    )

    # Расширенное поле: Диапазон времени (начало и конец бронирования)
    reservation_period = DateTimeRangeField(verbose_name='Время резервирования')

    def __str__(self):
        return f"{self.room_name}"