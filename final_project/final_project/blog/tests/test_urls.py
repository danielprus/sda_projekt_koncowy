from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)


class TestUrls(SimpleTestCase):
    def test_blog_home_url_resolves(self):
        url = reverse('blog-home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_user_posts_url_resolves(self):
        url = reverse('user-posts', args=['username'])
        self.assertEquals(resolve(url).func.view_class, UserPostListView)

    def test_post_detail_url_resolves(self):
        url = reverse('post-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_post_create_url_resolves(self):
        url = reverse('post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_post_update_url_resolves(self):
        url = reverse('post-update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_post_delete_url_resolves(self):
        url = reverse('post-delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)

    def test_about_url_resolves(self):
        url = reverse('blog-about')
        self.assertEquals(resolve(url).func, 'About')
