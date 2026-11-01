from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import MeetingRoom, Sessions, MeetingRoomRating, SessionRating, Team, Company

class TestViews(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')  
        self.client.login(username='testuser', password='12345')

        self.company = Company.objects.create(name='Test Company') 
        self.team = Team.objects.create(name='Test Team', company=self.company) 
        self.meeting_room = MeetingRoom.objects.create(
    room_name='Test Room',
    capacity=10,
    location='Test Location',
    available=True,
    company=self.company  # <-- Problematic line
)

        self.session = Sessions.objects.create(
            name='Test Session',
            team=self.team,
            meeting_room=self.meeting_room,
            date='2024-03-15',
            start_time='10:00',
            end_time='12:00'
        )

    def test_meeting_room_create_view(self):
        response = self.client.get(reverse('meeting-room-create'))
        self.assertEqual(response.status_code, 200)

        data = {
            'room_name': 'New Room',
            'capacity': 10,
            'location': 'New Location',
            'available': True,
            'company': self.Company
        }
        response = self.client.post(reverse('meeting-room-create'), data)
        self.assertEqual(response.status_code, 302)  

    def test_reserve_meeting_room_view(self):
        response = self.client.get(reverse('reserve-meeting-room'))
        self.assertEqual(response.status_code, 200)

        data = {
            'name': 'New Session',
            'team': self.team.id,
            'meeting_room': self.meeting_room,
            'date': '2024-03-16',
            'start_time': '10:00',
            'end_time': '12:00',
        }
        response = self.client.post(reverse('reserve-meeting-room'), data)
        self.assertEqual(response.status_code, 302)  
        self.team.manager = None
        self.team.save()
        response = self.client.post(reverse('reserve-meeting-room'), data)
        self.assertEqual(response.status_code, 302)  

    def test_meeting_room_rating_create_view(self):
        response = self.client.get(reverse('meeting-room-rating-create', kwargs={'pk': self.meeting_room.id}))
        self.assertEqual(response.status_code, 200)

        data = {
            'meeting_room': self.meeting_room.id,
            'score': 4,
            'comment': 'Nice room'
        }
        response = self.client.post(reverse('meeting-room-rating-create', kwargs={'pk': self.meeting_room.id}), data)
        self.assertEqual(response.status_code, 302)  

