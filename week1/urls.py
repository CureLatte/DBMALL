from django.urls import path
from . import views

urlpatterns =[
    path('', views.message_success, name='message_success'),
    path('user/', views.UserView.as_view(), name='UserView'),
    path('car/', views.CarView.as_view(), name='CarView'),
]