from django.http import JsonResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView

from book.models import Book
from book.serializer import BookReadSerializer, BookWriteSerializer
from user.permissions import CheckStaffUser, CheckLoginUser


class RegisterBookAPIView(APIView):
    permission_classes = [CheckLoginUser, CheckStaffUser]

    @swagger_auto_schema(tags=['책 등록'])
    def get(self, reqeust):
        book = Book.objects.all()
        serializer = BookReadSerializer(book, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(tags=['책 등록'])
    def post(self, request):
        serializer = BookWriteSerializer(data=request.data)

        if serializer.is_valid() is False:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return JsonResponse({'message': 'success'}, status=status.HTTP_200_OK)
