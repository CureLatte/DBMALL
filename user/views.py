from django.contrib.auth import authenticate, login
from django.core.exceptions import FieldError
from django.db import IntegrityError
from django.db.models import Model
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from blog.models import Article
from user.models import User, UserProfile


class UserSignupView(APIView):
    def post(self, request):
        data = {
            'message': 'Fail',
            'detail': ''
        }

        user_name = request.data.get('username', None)
        user_password = request.data.get('password', None)
        user_email = request.data.get('email', None)
        user_fullname = request.data.get('name', None)
        try:
            if User.objects.filter(username=user_name).exists():
                data['detail'] = '아이디 중복'
                return JsonResponse(data)
            user, created = User.objects.get_or_create(
                username=user_name,
                email=user_email,
                fullname=user_fullname
                )
            user.set_password(user_password)

            if created is False:
                data['detail'] = '이미 존재 하는 유저'
                return JsonResponse(data)
            else:
                user.save()
                data['message'] = 'success'
                data['detail'] = user.username
                return JsonResponse(data)

        except Exception as e:
            data['detail'] = e
            return JsonResponse(data)


class UserLoginView(APIView):
    def post(self, request):
        user_name = request.data.get('username', None)
        user_password = request.data.get('password', None)
        user = authenticate(request, username=user_name, password=user_password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated is False:
            fail_data = {
                'message' : 'User does not authenticated'
            }
            return JsonResponse(fail_data)

        profile = UserProfile.objects.get(user=user)
        articles = Article.objects.filter(writer=user)

        articles_data = {}

        for idx, article in enumerate(articles):
            category_list = article.category.all()
            category_data = []
            for category in category_list:
                category_data.append(category.subject)

            data = {
                'content' : article.content,
                'category': category_data,
            }

            articles_data[idx] = data

        response_data = {
            'username': user.username,
            'bio' : profile.bio,
            'articles': articles_data,
        }

        return JsonResponse(response_data)




