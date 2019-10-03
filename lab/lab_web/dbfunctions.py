from .models import *
from .forms import *


def add_doctor_function(name, contacts, comment):
    doctor = Doctors(name, contacts, comment)
    doctor.save()
    return doctor


def add_clinic_function(name, contacts, comment):
    clinic = Clinics(name, contacts, comment)
    clinic.save()
    return clinic


def add_order_function(request): # Конструкция try/except требует проверки
    try:
        order_form = OrderForm(request.POST)
        work_form = WorkInOrdersForm(request.POST)
        operations_form = OperationInOrdersForm(request.POST)
        files_form = FilesInOrdersForm(request.POST)
        all_forms = [order_form, work_form, operations_form, files_form]
        are_valid = True
        for i in all_forms:
            if not i.is_valid():
                are_valid = False
        if are_valid:
            order = order_form.save(commit='False')
            order.user = request.user
            order.save()
            for i in all_forms[1:]:
                i.save(commit='False')
                i.order = order
                i.save()
            return True
        return False
    except Exception as e:
        raise e

