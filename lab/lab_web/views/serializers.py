from rest_framework import serializers
from ..models import *

# from drf_extra_fields.relations import *

from .custom_fields import *

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
    material = PresentablePrimaryKeyRelatedField(presentation_serializer=MaterialSerializer,
                                                 queryset=Material.objects.all())

    class Meta:
        model = MaterialsOnStock
        exclude = ['user']


class MaterialUsedOnOperationSerializer(serializers.ModelSerializer):
    # operation = PresentablePrimaryKeyRelatedField(presentation_serializer=OperationSerializer,
    #                                               queryset=Operation.objects.all())
    material = PresentablePrimaryKeyRelatedField(presentation_serializer=MaterialSerializer,
                                                 queryset=Material.objects.all())

    class Meta:
        model = MaterialUsedOnOperation
        exclude = ['user', 'operation']


class OperationSerializer(serializers.ModelSerializer):
    # materials = PresentablePrimaryKeyRelatedField(presentation_serializer=MaterialSerializer,
    #                                              queryset=Material.objects.all(), many=True)
    materials = MaterialUsedOnOperationSerializer(many=True, required=False)

    class Meta:
        model = Operation
        exclude = ['user']


'''
{
    "materials": [{"material":3, "amount":3}],
    "operation_name": "qwwewq"
}
'''


class WorkSerializer(serializers.ModelSerializer):
    operations = PresentablePrimaryKeyRelatedField(presentation_serializer=OperationSerializer,
                                                   queryset=Operation.objects.all(), many=True)

    class Meta:
        model = Work
        exclude = ['user']


class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        exclude = ['user']


class OperationsInWorkSerializer(serializers.ModelSerializer):
    operation = PresentablePrimaryKeyRelatedField(presentation_serializer=OperationSerializer,
                                                  queryset=Operation.objects.all())
    work = PresentablePrimaryKeyRelatedField(presentation_serializer=WorkSerializer, queryset=Work.objects.all())

    class Meta:
        model = OperationsInWork
        exclude = ['user']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        exclude = ['user']


class OrderSerializer(serializers.ModelSerializer):
    doctor = PresentablePrimaryKeyRelatedField(presentation_serializer=DoctorSerializer, queryset=Doctor.objects.all())
    clinic = PresentablePrimaryKeyRelatedField(presentation_serializer=ClinicSerializer, queryset=Clinic.objects.all())
    work = PresentablePrimaryKeyRelatedField(presentation_serializer=WorkSerializer, queryset=Work.objects.all())
    operation = PresentablePrimaryKeyRelatedField(presentation_serializer=OperationSerializer,
                                                  queryset=Operation.objects.all())
    files = PresentablePrimaryKeyRelatedField(presentation_serializer=FileSerializer, queryset=File.objects.all())

    class Meta:
        model = Order
        exclude = ['user']


class WorkInOrdersSerializer(serializers.ModelSerializer):
    order = PresentablePrimaryKeyRelatedField(presentation_serializer=OrderSerializer, queryset=Order.objects.all())
    work = PresentablePrimaryKeyRelatedField(presentation_serializer=WorkSerializer, queryset=Work.objects.all())

    class Meta:
        model = WorkInOrders
        exclude = ['user']


class OperationsInOrdersSerializer(serializers.ModelSerializer):
    order = PresentablePrimaryKeyRelatedField(presentation_serializer=OrderSerializer, queryset=Order.objects.all())
    operations = PresentablePrimaryKeyRelatedField(presentation_serializer=Operation.objects.all(),
                                                   queryset=Operation.objects.all())

    class Meta:
        model = OperationsInOrders
        exclude = ['user']


class WorksPriceListSerializer(serializers.ModelSerializer):
    works = PresentablePrimaryKeyRelatedField(presentation_serializer=WorkSerializer, required=False)

    class Meta:
        model = WorksPriceList
        exclude = ['user']


class WorkPriceSerializer(serializers.ModelSerializer):
    price_list = PresentablePrimaryKeyRelatedField(presentation_serializer=WorksPriceListSerializer,
                                                   queryset=WorksPriceList.objects.all())
    work = PresentablePrimaryKeyRelatedField(presentation_serializer=WorkSerializer, queryset=Work.objects.all())

    class Meta:
        model = WorkPrice
        exclude = ['user']


class OperationsPriceListSerializer(serializers.ModelSerializer):
    operations = PresentablePrimaryKeyRelatedField(presentation_serializer=OperationSerializer,
                                                   queryset=Operation.objects.all())

    class Meta:
        model = OperationsPriceList
        exclude = ['user']


class OperationPriceSerializer(serializers.ModelSerializer):
    price_list = PresentablePrimaryKeyRelatedField(presentation_serializer=OperationsPriceListSerializer,
                                                   queryset=OperationsPriceList.objects.all())
    operation = PresentablePrimaryKeyRelatedField(presentation_serializer=OperationSerializer,
                                                  queryset=Operation.objects.all())

    class Meta:
        model = OperationPrice
        exclude = ['user']
