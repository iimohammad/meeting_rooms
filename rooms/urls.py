from django.urls import path
from .views import *

urlpatterns = [
    # Meeting Rooms CRUD
    path('meeting-room/create/', MeetingRoomCreateView.as_view(), name='meeting-room-create'),
    path('meeting-room/', MeetingRoomListView.as_view(), name='meeting-room-list'),
    path('meeting-room/update/<int:pk>/', MeetingRoomUpdateView.as_view(), name='meeting-room-update'),
    path('meeting-room/delete/<int:pk>/', MeetingRoomDeleteView.as_view(), name='meeting-room-delete'),
    path('meeting-room/detail/<int:pk>/', MeetingRoomDetailView.as_view(), name='meeting-room-detail'),

    # Reservation CRUD
    path('reserve', ReserveMeetingRoomView.as_view(), name='reserve'),
    path('show_reservations', Reservation_Show.as_view(), name='show_reservations'),
    path('cancel_reservation/<int:pk>/cancel/', Reservation_Cancel.as_view(), name='cancel_reservation'),

    # Handling Comments and Scores about Rooms
    path('meeting_room/<str:room_name>/ratings/', MeetingRoomRatingsView.as_view(), name='meeting_room_ratings'),
    #add rating for room
    #delete rating for room
    #edit rating for room
    #list of ratings for room

    # Handling Comments and Scores about Sessions
    # add rating for Sessions
    # delete rating for Sessions
    # edit rating for Sessions
    # list of ratings for Sessions
]
