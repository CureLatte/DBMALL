from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from blog.models import Article, Category
import datetime


class BlogMakeView(APIView):
    def post(self, request):
        user = request.user

        # 지난 날짜인지 확인
        today = datetime.datetime.now()
        print(today)
        print(type(user.join_date))
        print(datetime.timedelta(today.month, user.join_date.month))

        title = request.data.get('title')
        categories = request.data.get('category')
        categories_list = []
        for category in categories:
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


