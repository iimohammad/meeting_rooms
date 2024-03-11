from django.http import JsonResponse
from django.shortcuts import  redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from rooms.forms import MeetingRoomRatingForm
from .models import MeetingRoom, MeetingRoomRating, Sessions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MeetingRoom, Sessions
from .models import MeetingRoom
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class MeetingRoomListView(ListView , LoginRequiredMixin):
    model = MeetingRoom
    template_name = 'meeting_room_list.html'
    context_object_name = 'meeting_rooms'


class ReserveMeetingRoomView(CreateView , LoginRequiredMixin):
    model = Sessions
    fields = ['date', 'start_time', 'end_time']
    template_name = 'reserve_meeting_room.html'

    def form_valid(self, form):
        room_name = self.kwargs['room_name']
        room = get_object_or_404(MeetingRoom, room_name=room_name)

        # Check if the user is a manager
        if self.request.user.is_manager:
            # Check if the meeting room is available at the specified date and time
            date = form.cleaned_data['date']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            if room.is_available(date, start_time, end_time):
                # Create a new session for the reservation
                form.instance.team = self.request.user.team  # Assuming the user is associated with a team
                form.instance.meeting_room = room
                return super().form_valid(form)
            else:
                # Meeting room is not available, display an error message
                messages.error(self.request, 'The meeting room is not available at the specified date and time.')
                return redirect('error_url')
        else:
            # User is not a manager, display an error message
            messages.error(self.request, 'Only managers can reserve meeting rooms.')
            return redirect('error_url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_name = self.kwargs['room_name']
        context['room'] = get_object_or_404(MeetingRoom, room_name=room_name)
        return context


# @login_required
# class MeetingRoomRatingView(View):
#     def get(self, request, session_id):
#         session = get_object_or_404(Sessions, pk=session_id)
#         form = MeetingRoomRatingForm()
#         return render(request, 'meeting_room_rating_form.html', {'form': form, 'session': session})

#     def post(self, request, session_id):
#         session = get_object_or_404(Sessions, pk=session_id)
#         form = MeetingRoomRatingForm(request.POST)
#         if form.is_valid():
#             rating = form.save(commit=False)
#             rating.user = request.user
#             rating.meeting_room = session.meeting_room
#             rating.session = session
#             rating.save()
#             return redirect('success_url')
#         return render(request, 'meeting_room_rating_form.html', {'form': form, 'session': session})

class MeetingRoomRatingView(CreateView , LoginRequiredMixin):
    form_class = MeetingRoomRatingForm
    template_name = 'meeting_room_rating_form.html'
    success_url = reverse_lazy('meeting_room_list')





def stream_response():
    for i in range(100):
        yield f"{i}\\n"


@login_required
def cancel_reservation(request, session_id):
    # Retrieve the session object
    session = get_object_or_404(Sessions, pk=session_id)

    # Check if the current user is authorized to cancel the reservation
    if request.user.is_manager:
        # Attempt to cancel the reservation
        session.delete()
        return JsonResponse({'message': 'Reservation cancelled successfully.'})
    else:
        return JsonResponse({'error': 'Unauthorized to cancel reservation.'}, status=403)



class MeetingRoomSessionsListView(ListView , LoginRequiredMixin):
    model = Sessions
    template_name = 'meeting_room_sessions_list.html'
    context_object_name = 'sessions'

    def get_queryset(self):
        # Get the meeting room ID from the URL parameters
        meeting_room_id = self.kwargs['meeting_room_id']

        # Calculate the date range for the week
        today = datetime.now().date()
        end_of_week = today + timedelta(days=7)

        # Filter sessions for the specified meeting room and within the week
        queryset = Sessions.objects.filter(
            meeting_room=meeting_room_id,
            date__range=[today, end_of_week]
        ).order_by('date', 'start_time')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meeting_room_id'] = self.kwargs['meeting_room_id']
        return context



class SessionDetailView(DetailView ,LoginRequiredMixin):
    model = Sessions
    template_name = 'session_detail.html'
    context_object_name = 'session'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get all comments and ratings for this session
        session_id = self.object.id
        comments = MeetingRoomRating.objects.filter(meeting_room=self.object.meeting_room, session_id=session_id)

        context['comments'] = comments
        return context



class MeetingRoomRatingsView(DetailView , LoginRequiredMixin):
    model = MeetingRoom
    template_name = 'meeting_room_ratings.html'
    context_object_name = 'meeting_room'
    slug_field = 'room_name'
    slug_url_kwarg = 'room_name'

    def get_object(self, queryset=None):
        room_name = self.kwargs.get(self.slug_url_kwarg)
        queryset = self.get_queryset()
        return get_object_or_404(queryset, room_name=room_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve all ratings for the meeting room
        context['ratings'] = MeetingRoomRating.objects.filter(meeting_room=self.object)
        return context