from django.test import TestCase
import datetime
from user.models import User


# Create your tests here.
from blog.views import BlogMakeView


class TestBlogMake(TestCase):
    def test_blog_make_view_post(self):
        user = User.objects.create(
            username='user1',
            fullname='user1',
            email='user1@user1.user1'
        )

        user.set_password('user1')
        user.join_date = datetime.datetime(2022, 1, 1)

        user.save()

        user.login()
        request = {
            'user' : user,
            "title": "이글의 카테고리는 파이썬, 자바",
             "category" :[
                         "파이썬",
                            "자바"
                         ],
            "content": "테스트 2"
        }

        today = datetime.datetime.now()
        print(datetime.timedelta(today.month, user.join_date.month))

        self.assertIsNotNone(today)


