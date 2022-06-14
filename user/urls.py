from django.urls import include, path
from user.views import UserLoginView, UserDetailView, UserSignupView, UserLogoutView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('detail/', UserDetailView.as_view(), name='detail'),
    path('logout/', UserLogoutView.as_view(), name='logout')
]