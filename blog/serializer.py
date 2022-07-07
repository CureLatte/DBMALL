# from rest_framework import serializers
# from blog.models import Article, Category
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['subject']
#
#
# class ArticleSerializer(serializers.ModelSerializer):
#     article_set_reverse = serializers.SerializerMethodField()
#     category = CategorySerializer(many=True)
#
#     def get_article_set_reverse(self, obj):
#         return obj.writer.fullname
#
#     class Meta:
#         model = Article
#         fields = ['title', 'content', 'category', 'article_set_reverse']
#
