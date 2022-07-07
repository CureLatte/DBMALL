from django.urls import include, path
from user.views import UserLoginView, UserSignupView, UserDetailView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
]