from rest_framework import serializers
from book.models import Book


class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'writer', 'cost', 'cover_image', 'code']


class BookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'writer', 'cost', 'cover_image', 'code']