from django.urls import path

from blog.views import BlogMakeView

urlpatterns = [
    path('make/', BlogMakeView.as_view(), name='blog_make'),
]