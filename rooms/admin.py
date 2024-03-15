from django.contrib import admin
from rooms.models import *


@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):
    list_display = ['room_name', 'capacity', 'location', 'company', 'available']


@admin.register(Sessions)
class SessionsAdmin(admin.ModelAdmin):
    list_display = ['team', 'meeting_room', 'date', 'start_time', 'end_time']
