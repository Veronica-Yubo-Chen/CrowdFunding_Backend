from django.urls import path
from . import views

urlpatterns = [
    path('users/me/', views.CurrentUser.as_view(), name='current-user'),
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
]
