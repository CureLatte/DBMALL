from django.db import models


# Create your models here.
from user.models import User





class Article(models.Model):
    title = models.CharField(max_length=100, default='')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    category = models.ManyToManyField(Category)

    def __str__(self):
        if len(self.content) >= 10:
            cut = self.content[:10] + '...'
        else:
            cut = self.content
        return f'{cut}'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_created=True)
