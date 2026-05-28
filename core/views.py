from django.shortcuts import render
from .models import RoomReservation


def reservation_list_view(request):
    reservations = RoomReservation.objects.all().order_by('reservation_period')

    return render(request, 'core/reservations.html', {'reservations': reservations})