from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from .models import *
from .views import *


class TeamCreateViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = CustomUser.objects.create_user(username='AliStev', password='8318@8318')
        # Create a company
        self.company = Company.objects.create(name="Apple", phone="09334236754",
                                              address="One Apple Park Way, Cupertino, California")

    def test_team_creation(self):
        # Login the user
        self.client.login(username='AliStev', password='8318@8318')

        # Create a team
        response = self.client.post(reverse('create-team'), {
            'company': self.company.id,
            'name': 'Conference Room',
            'manager': self.user.id,
            'members': [self.user.id],
        })

        # Check if the team was created successfully
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Team.objects.filter(name='Conference Room').exists())
        self.assertEqual(Team.objects.filter(name='Conference Room')[0].company, self.company)
        self.assertEqual(Team.objects.filter(name='Conference Room')[0].name, 'Conference Room')
        self.assertEqual(Team.objects.filter(name='Conference Room')[0].manager, self.user)
        self.assertEqual(Team.objects.filter(name='Conference Room')[0].members.all()[0], self.user)

    def test_success_url(self):
        # Create a team
        team = Team.objects.create(name='Conference Room', company=self.company, manager=self.user)

        # Get the success URL
        view = TeamCreateView()
        view.object = team
        success_url = view.get_success_url()

        # Check if the success URL is correctly generated
        expected_url = reverse('team-list', kwargs={'company_id': team.company.id})
        self.assertEqual(success_url, expected_url)
