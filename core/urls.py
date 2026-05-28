from django.urls import path
from . import views

urlpatterns = [
    path('reservations/', views.reservation_list_view, name='reservations_list'),
]