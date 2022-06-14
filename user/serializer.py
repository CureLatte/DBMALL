from rest_framework import serializers

from blog.serializer import ArticleSerializer
from user.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio']


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article_set = ArticleSerializer(many=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'fullname', 'email', 'userprofile', 'article_set']
        extra_kwargs = {
            'password' : {
                'write_only': True
            },
        }
