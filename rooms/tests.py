from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Post, Author
from .forms import CreatePostForm  # اضافه کردن فرم مربوطه

def post_update(request, post_id):
    # View function for updating a post.
    # If the request method is GET, display the post update form.
    # If the request method is POST, validate the form and update the post if the form is valid.

    post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET':
        form = CreatePostForm(instance=post)
        return render(request, 'post/create_post.html', {'form': form})
    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully', 'success')
            return redirect('home:home')
        messages.error(request, 'There was an error in form validation.')
        return render(request, 'post/create_post.html', {'form': form})

class PostViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.author = Author.objects.create(user=self.user, phone_number='09123456789', country='test')

    def test_post_update_view_POST_valid_form(self):
        post = Post.objects.create(body='Original post body', author=self.user)

        data = {'body': 'Updated post body'}
        self.client.force_login(self.user)

        response = self.client.post(reverse('post:post_update', args=[post.id]), data)
        self.assertEqual(response.status_code, 302)  # 302 is the status code for redirect
        self.assertRedirects(response, reverse('home:home'))
        post.refresh_from_db()
        self.assertEqual(post.body, 'Updated post body')

    def test_post_update_view_GET(self):
        post = Post.objects.create(body='Original post body', author=self.user)

        self.client.force_login(self.user)

        response = self.client.get(reverse('post:post_update', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/create_post.html')
        self.assertContains(response, 'Original post body')

    def test_post_update_view_POST_invalid_form(self):
        post = Post.objects.create(body='Original post body', author=self.user)

        invalid_data = {'body': ''}
        self.client.force_login(self.user)

        response = self.client.post(reverse('post:post_update', args=[post.id]), invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')

        post.refresh_from_db()
        self.assertEqual(post.body, 'Original post body')
