from django.shortcuts import render
from rest_framework import viewsets
from .models import data
from .serializers import dataSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class dataViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = data.objects.all()
    serializer_class = dataSerializer
