from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ..models import Profile
from ..views import register, profile


class TestViews(TestCase):

    def test_register(self):
        response = self.client.post(reverse('/'), {'form': form})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')


    # def test_about_page_status(self):
    #     response = self.client.get('/about/')
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/about.html')

    # def test_post_list_view(self):
    #     response = self.client.get(reverse('blog-home'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertContains(response, 'testtitle')
    #     self.assertTemplateUsed(response, 'blog/home.html')

    # def test_user_post_list_view(self):
    #     response = self.client.get(reverse('user-posts', args=['testuser']))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertContains(response, 'testuser')
    #     self.assertTemplateUsed(response, 'blog/user_posts.html')
    
    # def test_post_detail_view(self):
    #     response = self.client.get(reverse('post-detail', kwargs={'pk': 1}))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertContains(response, 'testtitle')
    #     self.assertTemplateUsed(response, 'blog/post_detail.html')
