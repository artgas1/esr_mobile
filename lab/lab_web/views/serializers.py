from rest_framework import serializers
from ..models import *

from drf_extra_fields.relations import *

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
WorkPriceInPriceList -
WorksPriceList -
OperationsPriceInPriceList -
OperationsPriceList - 
MaterialsOnStock - MaterialsOnStockSerializer - MaterialsOnStockView
MaterialUsedOnOperation -  MaterialUsedOnOperationSerializer - MaterialUsedOnOperationView
'''


# Special field for filtering by user

class PresentablePrimaryKeyRelatedField(
    PresentableRelatedFieldMixin, PrimaryKeyRelatedField
):
    """
    Override PrimaryKeyRelatedField to represent serializer data instead of a pk field of the object.
    """
    def __init__(self, queryset, presentation_serializer):
        super(PresentablePrimaryKeyRelatedField, self).__init__()
        self.queryset = queryset

    def get_queryset(self):
        user = self.context['request'].user
        queryset = self.queryset.filter(user=user)
        return queryset


class UserFilteredPrimaryKey(serializers.PrimaryKeyRelatedField):
    def __init__(self, queryset):
        super(UserFilteredPrimaryKey, self).__init__()
        print(queryset)
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
    doctor = UserFilteredPrimaryKey(Doctor.objects.all())
    clinic = UserFilteredPrimaryKey(Clinic.objects.all())
    work = UserFilteredPrimaryKey(Work.objects.all())
    operations = UserFilteredPrimaryKey(Operation.objects.all())
    files = UserFilteredPrimaryKey(File.objects.all())

    class Meta:
        model = Order
        exclude = ['user']


class WorkInOrdersSerializer(serializers.ModelSerializer):
    order = UserFilteredPrimaryKey(Order.objects.all())
    work = UserFilteredPrimaryKey(Work.objects.all())

    class Meta:
        model = WorkInOrders
        exclude = ['user']


class OperationsInOrdersSerializer(serializers.ModelSerializer):
    order = UserFilteredPrimaryKey(Order.objects.all())
    operations = UserFilteredPrimaryKey(Operation.objects.all())

    class Meta:
        model = OperationsInOrders
        exclude = ['user']


class WorksPriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksPriceList
        exclude = ['user']


class WorkPriceSerializer(serializers.ModelSerializer):
    price_list = UserFilteredPrimaryKey(WorksPriceList.objects.all())
    work = UserFilteredPrimaryKey(Work.objects.all())

    class Meta:
        model = WorkPrice
        exclude = ['user']


class OperationsPriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationsPriceList
        exclude = ['user']


class OperationPriceSerializer(serializers.ModelSerializer):
    price_list = UserFilteredPrimaryKey(OperationsPriceList.objects.all())
    operation = UserFilteredPrimaryKey(Operation.objects.all())

    class Meta:
        model = OperationPrice
        exclude = ['user']

