from django.test import TestCase, RequestFactory, Client
import datetime

from blog.models import Category
from blog.views import BlogMakeView
from user.models import User, UserProfile
from django.utils import timezone


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

    def test_blog_make_view_post(self):
        # Given
        # 유저 로그인
        self.client.login(username=self.username, password=self.password)

        # request 요청 생성
        request = self.factory.get("/blog/make/article/")

        # category 생성
        category = Category.objects.create(subject='c1')
        category.save()
        category2 = Category.objects.create(subject='c2')
        category2.save()

        # When
        response = self.client.post(
            "/blog/make/article/",
            data={
                'category': ["c1", "c2"],
                'title' : 'test입니다.',
                'content': 'contenttest입니다. '
            }, format="json", content_type='application/json'
        )

        data = {
            'detail': '가입 후 1주일 이상 지난 사용자만 사용하실 수 있습니다.'
        }

        # Then
        self.assertDictEqual(response.json(), data)

    def test_blog_make_view_post_when_user_join_data_over_3days(self):
        # Given
        # 유저 로그인
        self.client.login(username=self.username, password=self.password)
        self.user.join_date = timezone.now() - datetime.timedelta(days=10)
        self.user.save()

        # request 요청 생성
        request = self.factory.get("/blog/make/article/")

        # category 생성
        category = Category.objects.create(subject='c1')
        category.save()
        category2 = Category.objects.create(subject='c2')
        category2.save()

        # When
        response = self.client.post(
            "/blog/make/article/",
            data={
                'category': ["c1", "c2"],
                'title': 'test입니다.',
                'content': 'contenttest입니다. '
            }, format="json", content_type='application/json'
        )

        data = {
            'message': 'success'
        }

        # Then
        self.assertDictEqual(response.json(), data)
