from rest_framework import serializers
from user.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio']


# 회원 가입 serializer
class UserSignUpSerializer(serializers.ModelSerializer):
    # User Model에 없는 값
    bio = serializers.CharField(max_length=100)

    def validate(self, validated_data):
        # 사용자가 이미 있을 경우
        email = validated_data.get('email')
        user_query = User.objects.filter(email=email)
        if user_query.exists():
            raise serializers.ValidationError
        return validated_data

    def create(self, validated_data):
        # 유저 생성시 User Profile 도 같이 생성
        bio = validated_data.pop('bio', '')
        user = User(**validated_data)
        user.save()
        userprofile = UserProfile.objects.create(user=user, bio=bio)
        userprofile.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'fullname', 'bio']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'fullname', 'email', 'userprofile']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }