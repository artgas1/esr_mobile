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

'''
Material
Doctor
Clinic
Operation
Work
OperationsInWork
Order
File
Technician
WorkInOrders
OperationInOrders
WorkPriceInPriceList
WorksPriceList
OperationPriceInPriceList
OperationPriceList
MaterialsOnStock
MaterialUsedOnOperation 
'''


class Material(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=100, choices=choices_materials_unit)
    limit = models.IntegerField()
    comment = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Materials"

    def __str__(self):
        return self.name


class Operation(models.Model):
    operation = models.CharField(max_length=100, unique=True)
    material = models.ManyToManyField(Material, through='MaterialUsedOnOperation')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Operations"

    def __str__(self):
        return self.operation


class Work(models.Model):
    work = models.CharField(max_length=100, unique=True)
    operations = models.ManyToManyField(Operation, through='OperationsInWork', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Works"

    def __str__(self):
        return self.work


class WorksPriceList(models.Model):
    price_list = models.CharField(max_length=100, unique=True)
    work = models.ManyToManyField(Work, through='WorkPrice', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Works Price Lists"

    def __str__(self):
        return '{}'.format(self.price_list)


class WorkPrice(models.Model):
    price_list = models.ForeignKey(WorksPriceList, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Work Price In Price List"

    def __str__(self):
        return '{} {} {}'.format(self.price_list, self.work, self.price)


class OperationsPriceList(models.Model):
    price_list = models.CharField(max_length=100)
    operation = models.ManyToManyField(Operation, through='OperationPrice', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Operations Price Lists"

    def __str__(self):
        return '{}'.format(self.price_list)


class OperationPrice(models.Model):
    price_list = models.ForeignKey(OperationsPriceList, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Operation Price In Price List"

    def __str__(self):
        return '{} {} {}'.format(self.price_list, self.operation, self.price)


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    price_list = models.ForeignKey(WorksPriceList, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Doctors"

    def __str__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    price_list = models.ForeignKey(WorksPriceList, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Clinics"

    def __str__(self):
        return self.name


class OperationsInWork(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Operations In Work'

    def __str__(self):
        return '{} {}'.format(self.work, self.operation)


class Order(models.Model):
    patient = models.CharField(max_length=50)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    work = models.ManyToManyField(Work, through='WorkInOrders')
    operations = models.ManyToManyField(Operation, through='OperationsInOrders')
    comment = models.CharField(max_length=100)
    progress = models.CharField(max_length=100, choices=choices_progress)
    deadline = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return '{} {} {}'.format(self.patient, self.doctor, self.clinic)


class File(models.Model):
    file = models.FileField(upload_to=get_file_path)
    order = models.ForeignKey(Order, related_name='files', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Files"

    def __str__(self):
        return self.file.name


class Technician(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    price_list = models.ForeignKey(OperationsPriceList, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Technicians"

    def __str__(self):
        return self.name


class WorkInOrders(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Work In Orders"

    def __str__(self):
        return '{} {}'.format(self.work, self.amount)


class OperationsInOrders(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    amount = models.IntegerField()
    deadline = models.DateField()
    is_done = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Operation In Orders"

    def __str__(self):
        return '{} {} {} {}'.format(self.operation, self.amount, self.technician, self.order)


class MaterialsOnStock(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Materials On Stock"

    def __str__(self):
        return '{} {}'.format(self.material, self.amount)


class MaterialUsedOnOperation(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Material Used on Operation"

    def __str__(self):
        return '{} {}'.format(self.operation, self.material)
