from django.urls import path
from . import views

urlpatterns = [
    # Home URL
    path('', views.index, name='index'),

    # User URLs
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list'),
    path('users/<int:user_id>/', views.UserDetailAPIView.as_view(), name='user-detail'),
    path('users/<int:user_id>/posts/', views.UserPostListAPIView.as_view(), name='user-post-list'),

    # Authentication URLs
    path('auth/login/',  views.LoginAPIView.as_view(), name='login'),
    path('auth/register/', views.RegisterAPIView.as_view(), name='register'),
    path('auth/logout/', views.LogoutAPIView.as_view(), name='logout'),

    # Post URLs
    path('posts/', views.PostListCreateAPIView.as_view(), name='post-list'),
    path('posts/<int:post_id>/', views.PostDetailAPIView.as_view(), name='post-detail'),
]
