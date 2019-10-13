from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from ..models import *
from .serializers import *
from rest_framework.permissions import *

'''
Models - Serializer - ViewSet 
Material - MaterialSerializer - MaterialView
Doctor - DoctorSerializer - DoctorView
Clinic - ClinicSerializer - ClinicView
Operation - OperationSerializer - OperationView
Work - WorkSerializer - WorkView
OperationsInWork - OperationsInWorkSerializer
Order - OrderSerializer - OrderView
File - FileSerializer - FileView
Technician - TechnicianSerializer - TechnicianView
WorkInOrders - WorkInOrdersSerializer - WorkInOrdersView
OperationInOrders - OperationsInOrdersSerializer - OperationsInOrdersView
WorksPriceList - 
OperationPriceList - 
MaterialsOnStock - MaterialsOnStockSerializer - MaterialsOnStockView
MaterialUsedOnOperation -  MaterialUsedOnOperationSerializer - MaterialUsedOnOperationView
'''


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


class WorkView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkSerializer

    def get_queryset(self):
        return Work.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print(serializer)
        serializer.save(user=self.request.user)


class OperationView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OperationSerializer

    def get_queryset(self):
        return Operation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TechnicianView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OperationSerializer

    def get_queryset(self):
        return Technician.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OperationsInWorkView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OperationsInWorkSerializer

    def get_queryset(self):
        return OperationsInWork.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MaterialUsedOnOperationView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MaterialUsedOnOperationSerializer

    def get_queryset(self):
        return MaterialUsedOnOperation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkInOrdersView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkInOrdersSerializer

    def get_queryset(self):
        return WorkInOrders.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OperationsInOrdersView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OperationsInOrdersSerializer

    def get_queryset(self):
        return OperationsInOrders.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
