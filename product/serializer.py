from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from product.models import Event, Product
from django.utils import timezone
from user.serializer import UserSerializer
from user.models import User


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


class ProductSerializer(serializers.ModelSerializer):

    def validate(self, data):
        print('validate!')
        if data.get('expose_end', '') < timezone.now():
            raise serializers.ValidationError(
                detail={'error': '노출 종료 일자는 현재 일자보다 이후여야 합니다. '}
            )
        return data

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        created_at = product.created_at.strftime('%Y-%m-%d %H:%M:%S')
        desc = product.desc
        desc += '\n' + created_at + '에 등록된 글입니다.'
        product.desc = desc
        product.save()
        return product

    class Meta:
        model = Product
        fields = ['writer', 'thumbnail', 'desc', 'expose_end', 'cost', 'active']