from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User, UserProfile
from user.serializer import UserSignUpSerializer, UserSerializer


@swagger_auto_schema(tag='유저_회원 가입')
class UserSignupView(APIView):
    def post(self, request):
        """
        로그인 했을 때
        :param request:
        :return: Json
        """
        # 유저 회원 만들기
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid() is False:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(tags=['유저_로그인'])
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

#
# # 사용자가 작성한 프로필, 게시글 보기
# class UserMyPageView(APIView):
#     # GET 요청
#     def get(self, request):
#         # 로그인 된 사용자
#         user = request.user
#
#         # 로그인 된 사용자가 아닐 경우
#         if user.is_authenticated is False:
#             fail_data = {
#                 'message' : 'User does not authenticated'
#             }
#             return JsonResponse(fail_data)
#
#         # 사용자가 작성한 프로필, 게시글 조회
#         profile = UserProfile.objects.filter(user=user)
#         if len(profile) == 0:
#             profile_bio = None
#         else:
#             profile_bio = profile[0].bio
#
#         articles = Article.objects.filter(writer=user)
#
#         # 조회한 게시글 정리 로직
#         articles_data = {}
#
#         for idx, article in enumerate(articles):
#             category_list = article.category.all()
#             category_data = []
#             for category in category_list:
#                 category_data.append(category.subject)
#
#             data = {
#                 'content' : article.content,
#                 'category': category_data,
#             }
#
#             articles_data[idx] = data
#
#         # 결과 응답
#         response_data = {
#             'username': user.username,
#             'bio' : profile_bio,
#             'articles': articles_data,
#         }
#
#         return JsonResponse(response_data)


class UserDetailView(APIView):
    def get(self, request, pk):
        user = User.objects.filter(pk=pk)

        if user.exists() is False:
            return JsonResponse({'message': '해당 유저가 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        user_serializer = UserSerializer(user.first())

        return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = User.objects.filter(pk=pk)

        if user.exists() is False:
            return JsonResponse({'message': '해당 유저가 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        user_serializer = UserSerializer(user.first(), data=request.data, partial=True)
        return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)
