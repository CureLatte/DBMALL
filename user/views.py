from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Article
from user.models import User, UserProfile
from user.serializer import UserSerializer


class UserSignupView(APIView):
    def post(self, request):
        # 응답 data set
        data = {
            'message': 'Fail',
            'detail': ''
        }

        # request 로부터 데이터 가져오기
        user_name = request.data.get('username', None)
        user_password = request.data.get('password', None)
        user_email = request.data.get('email', None)
        user_fullname = request.data.get('name', None)
        user_bio = request.data.get('bio', '')

        # 회원 가입 로직 시작
        try:
            # 아이디 중복 처리
            if User.objects.filter(username=user_name).exists():
                data['detail'] = '아이디 중복'
                return JsonResponse(data)

            user, created = User.objects.get_or_create(
                username=user_name,
                email=user_email,
                fullname=user_fullname
                )
            user.set_password(user_password)

            # 모든 정보가 똑같은 유저
            if created is False:
                data['detail'] = '이미 존재 하는 유저'
                return JsonResponse(data)

            # 새로운 회원일 경우
            else:
                user.save()
                profile = UserProfile.objects.create(user=user, bio=user_bio)
                profile.save()
                data['message'] = 'success'
                data['detail'] = user.username
                return JsonResponse(data)

        # 이외의 예외 처리
        except Exception as e:
            data['detail'] = e.args[0]
            return JsonResponse(data)


class UserLoginView(APIView):
    # post 요청
    def post(self, request):

        # request 로부터 data 받기
        user_name = request.data.get('username', None)
        user_password = request.data.get('password', None)

        # django 모듈의 인증
        user = authenticate(request, username=user_name, password=user_password)

        # 해당 유저가 없는 경우
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        # 로그인 시키기
        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        logout(request)
        return JsonResponse({'message': f'{user.username}님이 Logout했습니다. '})


# 사용자가 작성한 프로필, 게시글 보기
class UserDetailView(APIView):
    # GET 요청
    def get(self, request):
        # 로그인 된 사용자
        user = request.user

        # 로그인 된 사용자가 아닐 경우
        if user.is_authenticated is False:
            fail_data = {
                'message' : 'User does not authenticated'
            }
            return JsonResponse(fail_data)

        # 사용자가 작성한 프로필, 게시글 조회
        profile = UserProfile.objects.filter(user=user)
        if len(profile) == 0:
            profile_bio = None
        else:
            profile_bio = profile[0].bio

        articles = Article.objects.filter(writer=user)

        # 조회한 게시글 정리 로직
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

        # 결과 응답
        response_data = {
            'username': user.username,
            'bio' : profile_bio,
            'articles': articles_data,
        }

        return JsonResponse(response_data)


class UserInfoView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user).data
        return JsonResponse(serializer, status=status.HTTP_200_OK)

