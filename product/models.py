from django.db import models


# Create your models here.
class Event(models.Model):
    # 제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일, 활성화 여부
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(max_length=1000, default='/templates/static/image/default.jpg')
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    activate = models.BooleanField(default=False)
