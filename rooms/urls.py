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
    # path('reserve', ReserveMeetingRoomView.as_view(), name='reserve'),
    path('show_reservations', Reservation_Show.as_view(), name='show_reservations'),
    # path('cancel_reservation/<int:pk>/cancel/', Reservation_Cancel.as_view(), name='cancel_reservation'),

    # Handling Comments and Scores about Rooms
    path('meeting_room/<int:pk>/rate/', MeetingRoomRatingCreate.as_view(), name='rate_meeting_room'),
    path('meeting_room/rating/<int:pk>/update/', MeetingRoomRatingUpdate.as_view(),
         name='update_meeting_room_rating'),
    path('session/<int:pk>/rate/', SessionRatingCreate.as_view(), name='rate_session'),
    path('session/rating/<int:pk>/update/', SessionRatingUpdate.as_view(), name='update_session_rating'),

    path('room/<int:room_id>/comments/', RoomCommentsListView.as_view(), name='room_comments'),
    path('session/<int:session_id>/comments/', SessionCommentsListView.as_view(), name='session_comments'),
]
