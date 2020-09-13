from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ..models import Profile
from ..views import register, profile


class TestUsersViews(TestCase):

    def test_register(self):
        response = self.client.post(reverse('register'), {'form': 1})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
    
    def test_profile(self):
        response = self.client.post(reverse('profile'), {'form': 1})
        self.assertEquals(response.status_code, 302)
