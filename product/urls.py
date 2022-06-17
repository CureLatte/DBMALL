from django.urls import path

from product.views import EventView, EvnetNowView

urlpatterns = [
    path('event/', EventView.as_view(), name='event'),
    path('event/now/', EvnetNowView.as_view(), name='event_now')
]