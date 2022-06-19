from django.db import models

from user.models import User


class Event(models.Model):
    # 제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일, 활성화 여부
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(default='/templates/static/image/default.jpg')
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    activate = models.BooleanField(default=False)


class Product(models.Model):
    # 작성자, 썸네일, 상품 설명, 등록일자, 노출 종료 일자, 가격, 수정 일자, 활성화 여부
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="product", default='/templates/static/image/default.jpg')
    desc = models.CharField(max_length=1000)
    expose_end = models.DateTimeField()
    cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)


class Review(models.Model):
    # 작성자, 상품, 내용, 평점, 작성일
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField(default='')
    grade = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
