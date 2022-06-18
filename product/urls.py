from django.urls import path

from product.views import EventView, EvnetNowView, EventDetailView, ProductView

urlpatterns = [
    path('event/', EventView.as_view(), name='event'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_pk'),
    path('event/now/', EvnetNowView.as_view(), name='event_now'),
    path('product/', ProductView.as_view(), name='product'),

]