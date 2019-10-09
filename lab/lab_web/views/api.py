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
        doctors only for authenticated user
        """
        user = self.request.user
        return Doctor.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
