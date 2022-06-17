from rest_framework import serializers

from product.models import Event
from django.utils import timezone


class EventSerializer(serializers.ModelSerializer):

    def validate(self, data):
        # if data.get('start_at', '') < timezone.now():
        #     raise serializers.ValidationError(
        #         detail={'error': '시작 날짜는 오늘보다 이후 여야 합니다. '}
        #     )

        return data

    class Meta:
        model = Event
        fields = ['title', 'thumbnail', 'desc', 'start_at', 'end_at', 'activate']
        extra_kwargs = {
            'activate': {
                'write_only': True
            },
            'thumbnail': {
                'error_messages': {
                    'required': '썸네일 이미지를 넣어주세요',
                    'invalid': 'URL 형식이 아닙니다.'
                }
            },
            'desc': {
                'error_messages': {
                    'required': '이벤트 내용을 입력해 주세요',
                    'invalid': False,
                },
            }
        }