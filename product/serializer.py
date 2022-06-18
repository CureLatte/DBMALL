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
        print('create!')
        user_pk = validated_data.pop('writer')
        desc = validated_data.pop('desc')
        created_at = validated_data.get('created_at', '')

        desc += f'{created_at}에 등록된 상품 입니다.'

        user = User.objects.filter(pk=user_pk)
        print(user)
        if user.exists() is False:
            raise ObjectDoesNotExist

        product = Product(**validated_data)
        product.writer = user
        product.desc = desc
        product.save()

    class Meta:
        model = Product
        fields = ['writer', 'thumbnail', 'desc', 'expose_end', 'cost', 'active']