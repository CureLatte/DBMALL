from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from product.serializer import EventSerializer, ProductSerializer
from product.models import Event, Product
from rest_framework import status
from django.utils import timezone

from user.serializer import UserSerializer


class EventView(APIView):
    # 전체 이벤트 보기
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    # 이벤트 작성
    def post(self, request):
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return JsonResponse({'message': '정상'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 이벤트 수정 ( pk를 받아야됨 )
    def put(self, request):
        pk = request.data.get('pk', None)
        if pk is None:
            return JsonResponse({'message': '올바른 pk 값을 입력해 주세요'}, status=status.HTTP_400_BAD_REQUEST)
        event = Event.objects.filter(pk=pk)
        if len(event) == 0:
            return JsonResponse({'message': '해당 Event가 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        event_serializer = EventSerializer(event.first(), data=request.data, partial=True)
        if event_serializer.is_valid():
            event_serializer.save()
            return JsonResponse({'message': '정상'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(event_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)


class EventDetailView(APIView):
    # 한 이벤트
    def get(self, request, pk):
        event = Event.objects.filter(pk=pk)
        if event.exists() is False:
            return JsonResponse({'message': '없는 게시글 입니다.'})

        event_serializer = EventSerializer(event.first())
        return JsonResponse(event_serializer.data, status=status.HTTP_200_OK)

    # 해당 이벤트 수정정
    def put(self, request, pk):
        event = Event.objects.filter(pk=pk)
        if event.exists() is False:
            return JsonResponse({'message': '해당 이벤트가 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        event_serializer = EventSerializer(event.first(), request=request.data, partial=True)
        if event_serializer.is_valid():
            event_serializer.save()
            return JsonResponse({'message': '성공'})
        else:
            return JsonResponse(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EvnetNowView(APIView):
    def get(self, request):
        events = Event.objects.filter(start_at__lt=timezone.now(), end_at__gt=timezone.now())
        event_serializer = EventSerializer(events, many=True)
        return JsonResponse(event_serializer.data, safe=False, status=status.HTTP_200_OK)


class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        return JsonResponse(product_serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request):
        print(f'request: {request.data}')
        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid() is False:
            return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        product_serializer.save()
        return JsonResponse({'message': '성공!'}, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = Product.objects.filter(pk=pk)
        if product.exists() is False:
            return JsonResponse({'message': '해당 Product가 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        product_serializer = ProductSerializer(product.first())
        return JsonResponse(product_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = Product.objects.filter(pk=pk)
        if product.exists() is False:
            return JsonResponse({'message': '해당 Product가 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        product_serializer = ProductSerializer(product.first(), data=request.data, partial=True)
        if product_serializer.is_valid() is False:
            return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product_serializer.save()

        return JsonResponse({'message': '성공'}, status=status.HTTP_200_OK)