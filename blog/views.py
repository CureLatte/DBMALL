from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from blog.models import Article, Category
import datetime
from django.utils import timezone


# 게시글 작성 View
from user.permissions import RegistedMoreThanAWeekUser


class BlogMakeView(APIView):
    permission_classes = [RegistedMoreThanAWeekUser]

    def post(self, request):
        user = request.user

        # 지난 날짜인지 확인 ( Perminssion 배우기 전 )
        # if (timezone.now() - datetime.timedelta(days=3)) > user.join_date:
        #     return JsonResponse({'message': '글쓰기 권한이 없습니다.'})

        #
        title = request.data.get('title')
        categories = request.data.get('category')
        categories_list = []
        for category in categories:
            print(category)
            categories_list.append(Category.objects.get(subject=category).pk)

        content = request.data.get('content')

        article = Article.objects.create(
            writer=user,
            title=title,
            content=content,
        )
        article.category.set(categories_list)

        article.save()
        data = {
            'message': 'success'
        }

        return JsonResponse(data)


# 카테고리 추가
class CategoryAddView(APIView):
    def post(self, request):
        new_category = request.data.get('category', None)

        # category 입력을 못 받았을 경우
        if new_category is None:
            return JsonResponse({'message': 'Fail', 'detail': 'category를 입력해 주세요'})

        # category 저장
        category = Category.objects.create(subject=new_category)
        category.save()

        return JsonResponse({'message': 'Success'})