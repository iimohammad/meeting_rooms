from django.urls import path
from .views import *

urlpatterns = [
    # Meeting Rooms CRUD
    path('meeting-room/create/', MeetingRoomCreateView.as_view(), name='meeting-room-create'),
    path('meeting-room/', MeetingRoomListView.as_view(), name='meeting-room-list'),
    path('meeting-room/update/<int:pk>/', MeetingRoomUpdateView.as_view(), name='meeting-room-update'),
    path('meeting-room/delete/<int:pk>/', MeetingRoomDeleteView.as_view(), name='meeting-room-delete'),
    path('meeting-room/detail/<int:pk>/', MeetingRoomDetailView.as_view(), name='meeting-room-detail'),

    path('meeting_room/<str:room_name>/ratings/', MeetingRoomRatingsView.as_view(), name='meeting_room_ratings'),
    path('sessions/<int:pk>/', SessionDetailView.as_view(), name='session_detail'),
    path('meeting-rooms/<int:meeting_room_id>/sessions/', MeetingRoomSessionsListView.as_view(),
         name='meeting_room_sessions_list'),
    path('meeting-rooms/', MeetingRoomListView.as_view(), name='meeting_room_list'),
    path('sessions/<int:session_id>/cancel/', cancel_reservation, name='cancel_reservation'),
]
