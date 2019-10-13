from rest_framework import serializers
from ..models import *

'''

Models - Serializer - ViewSet 
Material - MaterialSerializer
Doctor - DoctorSerializer
Clinic - ClinicSerializer
Operation - OperationSerializer
Work - WorkSerializer
OperationsInWork - OperationsInWorkSerializer
Order - 
File - FileSerializer
Technician - TechnicianSerializer
WorkInOrders - 
OperationInOrders - 
WorksPriceList - 
OperationPriceList - 
MaterialsOnStock - MaterialsOnStockSerializer
MaterialUsedOnOperation -  MaterialUsedOnOperationSerializer
'''


# Special field for filtering by user
class UserFilteredPrimaryKey(serializers.PrimaryKeyRelatedField):
    def __init__(self, queryset):
        super(UserFilteredPrimaryKey, self).__init__()
        self.queryset = queryset

    def get_queryset(self):
        user = self.context['request'].user
        queryset = self.queryset.filter(user=user)
        return queryset


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ['user']


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        exclude = ['user']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        exclude = ['user']


class MaterialsOnStockSerializer(serializers.ModelSerializer):
    material = UserFilteredPrimaryKey(Material.objects.all())

    class Meta:
        model = MaterialsOnStock
        exclude = ['user']


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        exclude = ['user']


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        exclude = ['user']


class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        exclude = ['user']


class OperationsInWorkSerializer(serializers.ModelSerializer):
    operation = UserFilteredPrimaryKey(Operation.objects.all())
    work = UserFilteredPrimaryKey(Work.objects.all())

    class Meta:
        model = OperationsInWork
        exclude = ['user']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        exclude = ['user']


class MaterialUsedOnOperationSerializer(serializers.ModelSerializer):
    operation = UserFilteredPrimaryKey(Operation.objects.all())
    material = UserFilteredPrimaryKey(Material.objects.all())

    class Meta:
        model = MaterialUsedOnOperation
        exclude = ['user']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['user']
