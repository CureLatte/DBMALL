from django.urls import include, path
from user.views import UserLoginView, UserMyPageView, UserSignupView, UserDetailView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('mypage/', UserMyPageView.as_view(), name='mypage'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
]