from .models import *


def add_doctor(name, contacts, comment):
    doctor = Doctors(name, contacts, comment)
    doctor.save()
    return doctor


def add_clinic(name, contacts, comment):
    clinic = Clinics(name, contacts, comment)
    clinic.save()
    return clinic


def add_order(patient, doctor, clinic, comment, progress, deadline):
    pass
