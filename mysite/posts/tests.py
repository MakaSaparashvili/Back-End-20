from django.test import TestCase
from django.urls import reverse
from .models import BlogPost

class BlogPostModelTest(TestCase):
    def test_short_title_returns_full_when_less_than_or_equal_10(self):
        post = BlogPost.objects.create(title="ShortTit", content="x")
        self.assertEqual(post.short_title(), "ShortTit")

    def test_short_title_truncates_when_more_than_10(self):
        post = BlogPost.objects.create(title="ThisTitleIsLongerThanTen", content="x")
        self.assertEqual(post.short_title(), "ThisTitleI...")

class PostListViewTest(TestCase):
    def setUp(self):
        self.post = BlogPost.objects.create(title="My Test Post", content="content")

    def test_posts_page_status_code_and_contains_title(self):
        url = reverse('post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Test Post")
