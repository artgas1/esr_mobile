from django import forms
from django.contrib.auth.models import *

from .models import *


class UserFormRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'


class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinics
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'


class FilesInOrdersForm(forms.ModelForm):
    class Meta:
        model = FilesInOrders
        exclude = ['order']


class WorkInOrdersForm(forms.ModelForm):
    class Meta:
        model = WorkInOrders
        exclude = ['order']


class OperationInOrdersForm(forms.ModelForm):
    class Meta:
        model = OperationsInOrders
        exclude = ['order']
