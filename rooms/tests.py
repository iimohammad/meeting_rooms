from django.test import TestCase
from django.contrib.auth.models import get_user_model
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect , get_object_or_404
from .models import Team, Company, UserProfile, MeetingRoom, Reservation, Review
from .foarm import CreatePostForm  # اضافه کردن فرم مربوطه

def post_update(request, post_id):
    # View function for updating a post.
    # If the request method is GET, display the post update form.
    # If the request method is POST, validate the form and update the post if the form is valid.

    post = get_object_or_404(post, id=post_id)
    if request.method == 'GET':
        form = CreatePostForm(instance=post)
        return redirect(request, 'post/create_post.html', {'form': form})
    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully', 'success')
            return redirect('home:home')
        messages.error(request, 'There was an error in form validation.')
        return redirect(request, 'post/create_post.html', {'form': form})

class PostViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )

        # Create a test meeting room
        self.meeting_room = MeetingRoom.objects.create(
            room='Test Room',
            location='Test Location',
            capacity=10,
            available=True
        )

        # Create a test reservation
        self.reservation = Reservation.objects.create(
            user=self.user,
            room=self.meeting_room,
            date='2024-03-10',
            start_time='09:00',
            end_time='10:00',
            is_active=True,
            is_canceled=False,
            comment='Test Comment',
            otp='123456'
        )

        # Create a test review
        self.review = Review.objects.create(
            user=self.user,
            reservation=self.reservation,
            rating=5,
            comment='Test Review Comment'
        )

    def test_post_update_view_POST_valid_form(self):
        post = post.objects.create(body='Original post body', author=self.user)

        data = {'body': 'Updated post body'}
        self.client.force_login(self.user)

        response = self.client.post(reverse('post:post_update', args=[post.id]), data)
        self.assertEqual(response.status_code, 302)  # 302 is the status code for redirect
        self.assertRedirects(response, reverse('home:home'))
        post.refresh_from_db()
        self.assertEqual(post.body, 'Updated post body')
        self.assertEqual(self.meeting_room.room, 'Test Room')
        self.assertEqual(self.meeting_room.location, 'Test Location')
        self.assertEqual(self.meeting_room.capacity, 10)
        self.assertTrue(self.meeting_room.available)

    def test_post_update_view_GET(self):
        post = post.objects.create(body='Original post body', author=self.user)

        self.client.force_login(self.user)

        response = self.client.get(reverse('post:post_update', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/create_post.html')
        self.assertContains(response, 'Original post body')
        self.assertEqual(self.reservation.user, self.user)
        self.assertEqual(self.reservation.room, self.meeting_room)
        self.assertEqual(str(self.reservation.date), '2024-03-10')
        self.assertEqual(str(self.reservation.start_time), '09:00:00')
        self.assertEqual(str(self.reservation.end_time), '10:00:00')
        self.assertTrue(self.reservation.is_active)
        self.assertFalse(self.reservation.is_canceled)
        self.assertEqual(self.reservation.comment, 'Test Comment')
        self.assertEqual(self.reservation.otp, '123456')
        

    def test_post_update_view_POST_invalid_form(self):
        post = post.objects.create(body='Original post body', author=self.user)

        invalid_data = {'body': ''}
        self.client.force_login(self.user)

        response = self.client.post(reverse('post:post_update', args=[post.id]), invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')

        post.refresh_from_db()
        self.assertEqual(post.body, 'Original post body')
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.reservation, self.reservation)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, 'Test Review Comment')