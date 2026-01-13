from django.urls import path
from . import views

urlpatterns = [
    path('fundraisers/', views.FundraiserList.as_view(), name='fundraiser-list'),
    path('fundraisers/<int:pk>/', views.FundraiserDetail.as_view(), name='fundraiser-detail'),
    path('pledges/', views.PledgeList.as_view(), name='pledge-list'),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view(), name='pledge-detail'),
]