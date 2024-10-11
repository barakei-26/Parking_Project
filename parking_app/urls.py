from django.contrib import admin
from django.urls import path, include
from .views import BuildingListAPIView, BuildingDetailView

urlpatterns = [
    path('building/all', BuildingListAPIView.as_view(), name='building_list'),
    path('building/<int:pk>/', BuildingDetailView.as_view(), name='building')
]