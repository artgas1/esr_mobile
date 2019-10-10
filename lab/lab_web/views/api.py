from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from ..models import *
from .serializers import *
from rest_framework.permissions import *


class DoctorView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer

    def get_queryset(self):
        """
        doctors only for authenticated owner
        """
        return Doctor.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClinicView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ClinicSerializer

    def get_queryset(self):
        return Clinic.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MaterialView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MaterialSerializer

    def get_queryset(self):
        return Material.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MaterialsOnStockView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MaterialsOnStockSerializer

    def get_queryset(self):
        return MaterialsOnStock.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

