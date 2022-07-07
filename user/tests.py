from django.test import TestCase, RequestFactory, Client

from user.models import User, UserProfile


class TestBlogMake(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.email = 'usertest@usertesst.usertest'
        self.fullname = 'usettest'
        self.bio = 'thisisusettest'
        self.password = 'usettest'
        self.username = 'usettest'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
        )
        self.user.email = self.email
        self.user.fullname = self.fullname
        self.user.save()
        self.profile = UserProfile.objects.create(user=self.user, bio=self.bio)
        self.profile.save()


