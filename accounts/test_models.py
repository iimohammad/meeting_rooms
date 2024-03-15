from django.test import TestCase
from .models import CustomUser

class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password',
            phone='1234567890',
            address='123 Test St',
            gender='M',
            age=25,
            description='Test description'
        )

    def test_phone_field(self):
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.phone, '1234567890')

    def test_address_field(self):
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.address, '123 Test St')

    def test_gender_field(self):
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.gender, 'M')

    def test_age_field(self):
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.age, 25)

    def test_description_field(self):
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.description, 'Test description')