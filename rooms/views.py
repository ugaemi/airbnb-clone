from django.shortcuts import render

from rooms.models import Room


def all_rooms(request):
    all_rooms = Room.objects.all()
    return render(request, "rooms/home.html", context={'rooms': all_rooms})
