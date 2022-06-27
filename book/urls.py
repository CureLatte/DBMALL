from django.urls import path

from book.views import RegisterBookAPIView

urlpatterns = [
    path('register/', RegisterBookAPIView.as_view(), name='register_book')
]