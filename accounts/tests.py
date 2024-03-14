from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.forms import EditProfileForm
from .models import Post, Author  # Modified import statement

class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_user_registration(self):
        # Test user registration functionality
        new_user_data = {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
            'email': 'new@example.com'
        }
        response = self.client.post(reverse('signup_view'), data=new_user_data)
        self.assertEqual(response.status_code, 200)  # Check if the user is redirected after registration

    def test_user_login(self):
        # Test user login functionality
        response = self.client.post(reverse('login_view'), data=self.user_data)
        self.assertEqual(response.status_code, 302)  # Check if the user is redirected after login

    def test_profile_view(self):
        # Test profile view functionality
        self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        response = self.client.get(reverse('profile_view'))
        self.assertEqual(response.status_code, 200)  # Check if profile view returns status code 200
        self.assertContains(response, self.user_data['username'])  # Check if user data is present in profile

    def test_edit_profile(self):
        # Test editing profile functionality
        new_data = {
            'first_name': 'New',
            'last_name': 'User',
            'phone': '1234567890',
            'address': 'New Address',
            'age': 30,
            'description': 'New Description'
        }
        self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        response = self.client.post(reverse('edit_profile_view'), data=new_data)
        self.assertEqual(response.status_code, 200)  # Check if the user is redirected after editing profile
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, '')  # Check if profile data is updated correctly
