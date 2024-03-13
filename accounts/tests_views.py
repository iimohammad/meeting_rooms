from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='P@ssword1'
        )
        self.client.login(username='testuser', password='P@ssword1')

    def test_profile_view(self):
        response = self.client.get(reverse('profile_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User Name')
        self.assertContains(response, 'First Name')
        self.assertContains(response, 'Last Name')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Phone')

    def test_edit_profile_view(self):
        response = self.client.get(reverse('edit_profile_view'))
        self.assertEqual(response.status_code, 200)

    def test_custom_login_view(self):
        response = self.client.get(reverse('login_view'))
        # Check that the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)
        
        # Follow the redirect to the actual page (status code 200)
        response = self.client.get(response.url)
        self.assertEqual(response.status_code, 200)
        
    def test_signup_view(self):
        response = self.client.get(reverse('signup_view'))
        self.assertEqual(response.status_code, 200)
