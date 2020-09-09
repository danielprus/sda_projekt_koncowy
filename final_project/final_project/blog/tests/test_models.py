from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Post


class TestModel(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username='testuser')
        self.post1 = Post.objects.create(
            title='post1',
            content='aaaaaa',
            date_posted='',
            author=self.assertTrue(Author.objects.get(user=user))
        )

    def test_post(self):
        self.assertEquals(self.post1, 'post1')
