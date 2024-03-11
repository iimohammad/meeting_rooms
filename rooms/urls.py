from django.urls import path
from .views import MeetingRoomListView, MeetingRoomRatingsView, \
    MeetingRoomSessionsListView, SessionDetailView, cancel_reservation

urlpatterns = [
    path('meeting_room/<str:room_name>/ratings/', view=MeetingRoomRatingsView.as_view(), \
        name='meeting_room_ratings'),
    path('sessions/<int:pk>/', SessionDetailView.as_view(), name='session_detail'),
    path('meeting-rooms/<int:meeting_room_id>/sessions/', MeetingRoomSessionsListView.as_view(), \
        name='meeting_room_sessions_list'),
    path('meeting-rooms/', MeetingRoomListView.as_view(), name='meeting_room_list'),
    path('sessions/<int:session_id>/cancel/', cancel_reservation, name='cancel_reservation'),
]