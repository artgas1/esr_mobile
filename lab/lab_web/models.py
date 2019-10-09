from django.db import models
from django.contrib.auth.models import User

# Create your models here.

import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext)
    return os.path.join('uploads/documents', filename)


choices_progress = {
    ('NR', 'Не готов'),
    ('HR', 'Частично готов'),
    ('R', 'Готов')
}

choices_materials_unit = {
    ('gr', 'гр.'),
    ('sht', 'шт.')
}


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Doctors"


class Clinic(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Clinics"


class Order(models.Model):
    patient = models.CharField(max_length=50)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    progress = models.CharField(max_length=100, choices=choices_progress)
    deadline = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Orders"


class FilesInOrders(models.Model):
    file = models.FileField(upload_to=get_file_path)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Files In Orders"


class Work(models.Model):
    work = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Works"


class WorkInOrders(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    amount = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Work In Orders"


class Operation(models.Model):
    operation = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Operations"


class Technician(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Technicians"


class OperationsInOrders(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    amount = models.IntegerField()
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    deadline = models.DateField()
    is_done = models.BooleanField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Operation In Orders"


class OperationsInWork(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Operations In Works"


class WorksPriceList(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, blank=True)
    price_list = models.CharField(max_length=100)
    price = models.IntegerField()
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Works Price Lists"


class OperationsPriceList(models.Model):
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    price = models.IntegerField()
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Operations Price Lists"


class Material(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100, choices=choices_materials_unit)
    limit = models.IntegerField()
    comment = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Materials"


class MaterialsOnStock(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Materials On Stock"


class MaterialUsedOnOperation(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Materials Used on Operation"
