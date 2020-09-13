from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from ..models import Profile


class TestUsersModels(TestCase):

    def setUp(self):
        Profile.objects.create(
            user = get_user_model().objects.create_user(username='testuser'),
            # user = User.objects.create(username='testuser'),
            image = 'default.jpg'
            )

    def test_profile(self):
        post = Profile.object.get(id=1)
        self.assertEquals(post.username, 'testuser')
        # self.assertEquals(str(profile), 'testuser')
