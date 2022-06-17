from django.urls import include, path
from user.views import UserLoginView, UserDetailView, UserSignupView, UserInfoView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('detail/', UserDetailView.as_view(), name='detail'),
    path('info/', UserInfoView.as_view(), name='user_info')
]