from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import MeetingRoom, Sessions, MeetingRoomRating, SessionRating

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_meeting_room_list_view(self):
        response = self.client.get(reverse('meeting-room-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meeting_room_list.html')

    def test_meeting_room_detail_view(self):
        meeting_room = MeetingRoom.objects.create(room_name='Test Room', capacity=10, location='Test Location', available=True)
        response = self.client.get(reverse('meeting-room-detail', args=[meeting_room.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_view_room.html')

    def test_reserve_meeting_room_view(self):
        response = self.client.get(reverse('reserve-meeting-room'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reserve_meeting_room.html')

    def test_reservation_show_view(self):
        response = self.client.get(reverse('show-reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'session_list.html')

    def test_reservation_cancel_view(self):
        meeting_room = MeetingRoom.objects.create(room_name='Test Room', capacity=10, location='Test Location', available=True)
        session = Sessions.objects.create(name='Test Session', meeting_room=meeting_room, date='2024-03-15', start_time='09:00:00', end_time='10:00:00')
        response = self.client.get(reverse('cancel-reservation', args=[session.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'session_confirm_delete.html')

    def test_meeting_room_rating_create_view(self):
        meeting_room = MeetingRoom.objects.create(room_name='Test Room', capacity=10, location='Test Location', available=True)
        response = self.client.post(reverse('meeting-room-rating-create', args=[meeting_room.pk]), {'score': 4, 'comment': 'Test Comment'})
        self.assertEqual(response.status_code, 302)  # Redirects upon success

    def test_session_rating_create_view(self):
        meeting_room = MeetingRoom.objects.create(room_name='Test Room', capacity=10, location='Test Location', available=True)
        session = Sessions.objects.create(name='Test Session', meeting_room=meeting_room, date='2024-03-15', start_time='09:00:00', end_time='10:00:00')
        response = self.client.post(reverse('session-rating-create', args=[session.pk]), {'score': 4, 'comment': 'Test Comment'})
        self.assertEqual(response.status_code, 302)  # Redirects upon success

    def test_meeting_room_rating_update_view(self):
        meeting_room = MeetingRoom.objects.create(room_name='Test Room', capacity=10, location='Test Location', available=True)
        rating = MeetingRoomRating.objects.create(user=self.user, meeting_room=meeting_room, score=3)
        response = self.client.post(reverse('meeting-room-rating-update', args=[rating.pk]), {'score': 5, 'comment': 'Updated Comment'})
        self.assertEqual(response.status_code, 302)  # Redirects upon success

    def test_session_rating_update_view(self):
        meeting_room = MeetingRoom.objects.create(room_name='Test Room', capacity=10, location='Test Location', available=True)
        session = Sessions.objects.create(name='Test Session', meeting_room=meeting_room, date='2024-03-15', start_time='09:00:00', end_time='10:00:00')
        rating = SessionRating.objects.create(user=self.user, session=session, score=3)
        response = self.client.post(reverse('session-rating-update', args=[rating.pk]), {'score': 5, 'comment': 'Updated Comment'})
        self.assertEqual(response.status_code, 302)  # Redirects upon success
