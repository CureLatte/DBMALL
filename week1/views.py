from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import permissions

from .models import User, Car, GameProfile


@csrf_exempt
# Create your views here.
def message_success(request):
    data = {
        'message': 'success'
    }
    return JsonResponse(data)


class UserView(View):
    @staticmethod
    def get(self, request):
        user_list = User.objects.all()

        data = {
            'result': user_list
        }
        return JsonResponse(data)

    @staticmethod
    def post(self, request):
        username = request.POST['username']
        user = User.objects.create(name=username)
        user.save()
        data = {
            'result': 'success'
        }
        return JsonResponse(data)


class AllowAny(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class CarView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(self, request):
        car_list = Car.objects.all()
        data = {
            'result': car_list
        }
        return JsonResponse(data)

    @staticmethod
    def post(self, request):
        data = {
            'result': 'success'
        }

        user_pk = request.post['user']
        if User.objects.filter(user_pk).exists():
            user = User.objects.get(user_pk)
            car_name = request.post['car_name']
            car = Car.objects.create(user=user, car_name=car_name)
            car.save()
        else:
            data['result'] = 'fail'

        return JsonResponse(data)


