from django.test import TestCase, Client
from django.urls import reverse
from ..views import home
import json


class TestViews(TestCase):
    def test_home_view(self):
        client = Client()
        response = self.client.get('your_server_ip:8000')
        self.assertEquals(response.status_code, 200)

    def test_post_list_view(self):
        client = Client()
        response = self.client.get(reverse(''))