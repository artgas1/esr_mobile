from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login as auth_login
from .decorators import *
from django.conf import settings

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect


@anonymous_required
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)  # put main page
            else:
                return HttpResponse("Your account is inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'auth/login.html')


@anonymous_required
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserFormRegistration(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserFormRegistration()
    return render(request, 'auth/registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def add_order(request):
    # files in orders
    # work in orders
    # operations_in_orders
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        work_form = WorkInOrdersForm(request.POST)
        operations_form = OperationInOrdersForm(request.POST)
        files_form = FilesInOrdersForm(request.POST)
        forms = [order_form, work_form, operations_form, files_form]
        are_valid = True
        for i in forms:
            if not i.is_valid():
                are_valid = False
        if are_valid:
            order = order_form.save()
            for i in forms[1:]:
                i.save(commit='False')
                i.order = order

    return render(request, 'add_order.html',
                  {'order': OrderForm, 'work': WorkInOrdersForm, 'operations': OperationInOrdersForm,
                   'files': FilesInOrdersForm})
