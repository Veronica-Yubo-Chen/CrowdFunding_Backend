from django.urls import path
from . import views

urlpatterns = [
    path('', views.FundraiserList.as_view(), name='fundraiser-list'),
    path('fundraisers/<int:pk>/', views.FundraiserDetail.as_view()),
    path('pledges/', views.PledgeList.as_view())
]