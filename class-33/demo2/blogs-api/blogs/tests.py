from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Blog


class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test_user', password='pass')
        test_user.save()

        test_thing = Blog.objects.create(author=test_user, title="Thing2", body="A thing")
        test_thing.save()

    def test_things_model(self):
        thing = Blog.objects.get(id=1)
        actual_author = str(thing.author)
        actual_title = str(thing.title)
        actual_body = str(thing.body)
        self.assertEqual(actual_author, "test_user")
        self.assertEqual(actual_title, "Thing2")
        self.assertEqual(actual_body, "A thing")
