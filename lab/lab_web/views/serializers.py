from rest_framework import serializers
from ..models import *


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
    material = MaterialSerializer(read_only=True)

    class Meta:
        model = MaterialsOnStock
        exclude = ['user']