from rest_framework import serializers
from user.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio']


class UserSignUpSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    def validate(self, validated_data):
        email = validated_data.get('email')
        user_query = User.objects.filter(email=email)
        if user_query.exists():
            raise serializers.ValidationError
        return validated_data

    class Meta:
        model = User
        fields = ['username', 'password', 'fullname', 'email']
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