
import csv
import json
from time import sleep

from django.http import JsonResponse, FileResponse, StreamingHttpResponse, HttpResponse
from django.shortcuts import render ,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import MeetingRoom, Reservation, Review, Company, UserProfile
from django.contrib.auth.decorators import login_required

def meeting_room_list(request):
     return render(list(MeetingRoom.objects.all().values()), safe=False)

def meeting_room_detail(request, room_id):
    return render(request, 'meeting_room_detail.html', {'room': get_object_or_404(MeetingRoom, id=room_id)})

def reserve_room(request, room_id):
    Reservation.objects.create(room=get_object_or_404(MeetingRoom, id=room_id), user=request.user)
    return render('meeting_room_detail', room_id=room_id)

def add_review(request, room_id):
    Review.objects.create(room=get_object_or_404(MeetingRoom, id=room_id), user=request.user)
    return render('meeting_room_detail', room_id=room_id)

def stream_response():
    for i in range(100):
        yield f"{i}\\n"
streaming_response = StreamingHttpResponse(stream_response())
print(f"Type of StreamingHttpResponse: {type(streaming_response)}")
http_response = HttpResponse("This is a simple HTTP response")
print(f"Type of HttpResponse: {type(http_response)}")

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
    
def company_list(request):
    return render(request, 'company_list.html', {'companies': Company.objects.all()})

def user_profile(request, user_id):
    return render(request, 'user_profile.html', {'user_profile': get_object_or_404(UserProfile, user_id=user_id)})

def review_list(request):
    return render(request, 'review_list.html', {'reviews': Review.objects.filter(user=request.user)})

@csrf_exempt
@require_http_methods(['POST'])
def reserve_room(request, room_id):
    Reservation.objects.create(room=get_object_or_404(MeetingRoom, id=room_id), user=request.user)
    return JsonResponse('meeting_room_detail', room_id=room_id)

@csrf_exempt
@require_http_methods(['POST'])
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.is_canceled = True
    reservation.save()
    return JsonResponse('meeting_room_detail', room_id=reservation.room.id)