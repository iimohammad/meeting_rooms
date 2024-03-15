import csv
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from .models import MeetingRoom, Sessions
from time import sleep
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MeetingRoom, Sessions
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.views import View
from django.utils.decorators import method_decorator
from .foarm import ReserveMeetingRoomForm, MeetingRoomRatingForm
from django.contrib import messages
from django.shortcuts import redirect
from company.models import *
from company.utils.decorators import *


# CRUD Meeting Rooms
@method_decorator(login_required, name='dispatch')
@method_decorator(manager_required, name='dispatch')
class MeetingRoomCreateView(CreateView):
    model = MeetingRoom
    fields = ['room_name', 'capacity', 'location', 'available', 'company']
    success_url = reverse_lazy('meeting-room-list')
    template_name = 'meeting_room_create.html'


@method_decorator(login_required, name='dispatch')
class MeetingRoomListView(ListView):
    model = MeetingRoom
    template_name = 'meeting_room_list.html'
    context_object_name = 'meeting_room'


@method_decorator(login_required, name='dispatch')
class MeetingRoomDetailView(DetailView):
    model = MeetingRoom
    template_name = 'detail_view_room.html'
    context_object_name = 'meeting_room'


@method_decorator(login_required, name='dispatch')
@method_decorator(manager_required, name='dispatch')
class MeetingRoomUpdateView(UpdateView):
    model = MeetingRoom
    fields = ['room_name', 'capacity', 'location', 'available', 'company']
    success_url = reverse_lazy('meeting-room-list')
    template_name = 'meeting_room_update.html'


@method_decorator(login_required, name='dispatch')
@method_decorator(check_company_manager, name='dispatch')
class MeetingRoomDeleteView(DeleteView):
    model = MeetingRoom
    success_url = reverse_lazy('meeting-room-list')
    template_name = 'meeting_room_confirm_delete.html'


@method_decorator(login_required, name='dispatch')
class MeetingRoomListView(ListView):
    model = MeetingRoom
    template_name = 'meeting_room_list.html'
    context_object_name = 'meeting_rooms'


# Reserve A Meeting Room for a Session
@method_decorator(login_required, name='dispatch')
@method_decorator(manager_required, name='dispatch')
class ReserveMeetingRoomView(CreateView):
    model = Sessions
    form_class = ReserveMeetingRoomForm
    template_name = 'reserve_meeting_room.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        reservation = form.save(commit=False)

        # Fetch the team managed by the current user (manager)
        # manager_team = Team.objects.filter(manager=self.request.user).first()

        if self.request.user.teams:
            reservation.team = self.request.user.teams
            reservation.save()
            messages.success(self.request, 'Meeting room reserved successfully.')
            return super().form_valid(form)
        else:
            # If no team is managed by the user, display an error message
            messages.error(self.request, 'You are not managing any team.')
            return redirect('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meeting_rooms'] = MeetingRoom.objects.filter(available=True)
        return context


@method_decorator(login_required, name='dispatch')
class Reservation_Show(ListView):
    model = Sessions
    template_name = 'session_list.html'
    context_object_name = 'sessions'

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.GET.get('date')
        room_name = self.request.GET.get('room')

        if date:
            queryset = queryset.filter(date=date)
        if room_name:
            queryset = queryset.filter(meeting_room__room_name=room_name)

        queryset = queryset.order_by('date', 'start_time')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        distinct_room_names = set(session.meeting_room.room_name for session in context['sessions'])
        context['distinct_room_names'] = distinct_room_names
        return context


@method_decorator(login_required, name='dispatch')
@manager_required(manager_required, name='dispatch')
class Reservation_Cancel(DeleteView):
    model = Sessions
    success_url = reverse_lazy('show_reservations')
    template_name = 'session_confirm_delete.html'


# Handling Comments and Scores about rooms and sessions

@method_decorator(login_required, name='dispatch')
class MeetingRoomRatingCreate(CreateView):
    model = MeetingRoomRating
    fields = ['meeting_room', 'score', 'comment']
    template_name = 'meeting_room_rating_form.html'
    success_url = reverse_lazy('meeting-room-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.meeting_room_id = self.kwargs['pk']
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class SessionRatingCreate(CreateView):
    model = SessionRating
    fields = ['score', 'comment']
    template_name = 'session_rating_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.session_id = self.kwargs['pk']
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class MeetingRoomRatingUpdate(UpdateView):
    model = MeetingRoomRating
    fields = ['score', 'comment']
    template_name = 'meeting_room_rating_form.html'
    success_url = reverse_lazy('meeting-room-list')


@method_decorator(login_required, name='dispatch')
class SessionRatingUpdate(UpdateView):
    model = SessionRating
    fields = ['score', 'comment']
    template_name = 'session_rating_form.html'
    success_url = reverse_lazy('show_reservations')


@method_decorator(login_required, name='dispatch')
class RoomCommentsListView(ListView):
    template_name = 'room_comments.html'
    context_object_name = 'room_ratings'

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return MeetingRoomRating.objects.filter(meeting_room_id=room_id)


@method_decorator(login_required, name='dispatch')
class SessionCommentsListView(ListView):
    template_name = 'session_comments.html'
    context_object_name = 'session_ratings'

    def get_queryset(self):
        session_id = self.kwargs['session_id']
        return SessionRating.objects.filter(session_id=session_id)
