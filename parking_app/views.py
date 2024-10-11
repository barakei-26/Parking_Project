from typing import Any
from django.shortcuts import render
from .models import Building, Slot, Floor
from .serializers import BuildingSerializer, BuildingResumeSerializer
from django.views.generic import ListView, DetailView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

class BuildingListAPIView(ListCreateAPIView):
    queryset =  Building.objects.all()
    serializer_class = BuildingSerializer
    
    def get(self, request):
        if not Building.objects.exists():
            return Response({"detail": "No buildings available."}, status=status.HTTP_404_NOT_FOUND)


        serializer = BuildingResumeSerializer(Building.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     

class BuildingDetailView(APIView):
    def get(self, request, pk):
        # Get the object by primary key or return 404 if not found
        building = get_object_or_404(Building, pk=pk)

        # Serialize the object
        serializer = BuildingSerializer(building)

        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
        


