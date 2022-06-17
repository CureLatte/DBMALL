from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from product.serializer import EventSerializer
from product.models import Event
from rest_framework import status
from django.utils import timezone


class EventView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def post(self, request):
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return JsonResponse({'message': '정상'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


class EvnetNowView(APIView):
    def get(self, request):
        events = Event.objects.filter(start_at__lt=timezone.now(), end_at__gt=timezone.now())
        event_serializer = EventSerializer(events, many=True)
        return JsonResponse(event_serializer.data, safe=False, status=status.HTTP_200_OK)

