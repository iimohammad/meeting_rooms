from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import MeetingRoom, Reservation, UserProfile, Company , Review
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def index(request):
    rooms = MeetingRoom.objects.all()
    return render(request, 'index.html', {'rooms': rooms})

@login_required
def reserve_room(request, room_id):
    if request.method == 'POST':
        room = MeetingRoom.objects.get(id=room_id)
        reservation = Reservation(user=request.user, room=room)
        reservation.save()
        return HttpResponse('Reservation made successfully')
    else:
        return HttpResponse('Invalid request')

@login_required
def cancel_reservation(request, reservation_id):
    if request.method == 'POST':
        reservation = Reservation.objects.get(id=reservation_id)
        if reservation.user == request.user:
            reservation.delete()
            return HttpResponse('Reservation cancelled successfully')
        else:
            return HttpResponse('You do not have permission to cancel this reservation')
    else:
        return HttpResponse('Invalid request')

@login_required
def room_status(request, room_id):
    room = get_object_or_404(MeetingRoom, id=room_id)
    reservations = Reservation.objects.filter(room=room)
    return render(request, 'room_status.html', {'room': room, 'reservations': reservations})

@login_required
def add_review(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(MeetingRoom, id=room_id)
        reservation = Reservation.objects.get(user=request.user, room=room)
        reservation.score = request.POST['score']
        reservation.review = request.POST['review']
        reservation.save()
        return HttpResponseRedirect(reverse('room_status', args=(room.id,)))
    else:
        return HttpResponse('Invalid request')

@login_required
def add_review(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(MeetingRoom, id=room_id)
        review = Review(user=request.user, room=room, rating=request.POST['rating'], comment=request.POST['comment'])
        review.save()
        return HttpResponseRedirect(reverse('room_status', args=(room.id,)))
    else:
        return HttpResponse('Invalid request')