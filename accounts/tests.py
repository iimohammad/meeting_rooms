# tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

class UserTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword',
            'phone': '09123456789',
        }

        self.updated_user_data = {
            'first_name': 'Updated',
            'last_name': 'UserUpdated',
            'phone': '09876543210',
        }

        self.profile_image = SimpleUploadedFile(
            'test_image.jpg',
            b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00\x01\x00\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\tpHYs\x00\x00\n\x00\n\x00\x01\x00\x00\x00\x00\xa4\x7f\x00\x00\x00\x00IEND\xaeB`\x82'
        )

        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.login(username=self.user_data['username'], password=self.user_data['password'])

    def test_signup_view(self):
        response = self.client.get(reverse('signup_view'))
        self.assertEqual(response.status_code, 200)

        # Test user registration
        response = self.client.post(reverse('signup_view'), data=self.user_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile')

        # Test user login after registration
        self.client.logout()
        response = self.client.post(reverse('login_view'), data=self.user_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile')

    def test_profile_view(self):
        response = self.client.get(reverse('profile_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test User')

    def test_edit_profile_view(self):
        response = self.client.get(reverse('edit_profile_view'))
        self.assertEqual(response.status_code, 200)

        # Test updating user profile
        response = self.client.post(reverse('edit_profile_view'), data=self.updated_user_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Updated UserUpdated')

    def test_email_login_view(self):
        response = self.client.get(reverse('email_login_view'))
        self.assertEqual(response.status_code, 200)

        # Assuming OTP is sent to the email, you can modify this test accordingly
        response = self.client.post(reverse('email_login_view'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter OTP')

        # Additional test cases for OTP verification can be added here

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_upload_profile_image(self):
        response = self.client.post(reverse('edit_profile_view'), data={'profile_image': self.profile_image})
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertTrue(self.user.profile_image)

# Additional test cases for form validation, edge cases, etc., can be added as needed
