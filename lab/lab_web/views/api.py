from rest_framework import viewsets, views
from ..models import *
from .serializers import *
from rest_framework.permissions import *
from rest_framework.response import Response
from django.conf import settings
import datetime
from rest_framework.exceptions import ParseError, NotFound

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
WorksPriceList - 
OperationPriceList - 
MaterialsOnStock - MaterialsOnStockSerializer - MaterialsOnStockView
MaterialUsedOnOperation -  MaterialUsedOnOperationSerializer - MaterialUsedOnOperationView
'''


def convert_to_datetime(string):
    try:
        if not string:
            return None
        else:
            date = datetime.datetime.strptime(string, settings.INPUT_OUTPUT_DATE_FORMAT)
            return date
    except Exception as e:
        raise ParseError(detail='Date has to be in {} format'.format(settings.INPUT_OUTPUT_DATE_FORMAT))


def check_is_int(string, instance_name):
    if not string.isdigit():
        raise ParseError(detail='{} param has to be int or pk'.format(instance_name))
    else:
        query_filter = int(string)
        return query_filter


def filter_by_date(queryset, start_date_filter, end_date_filter):
    if start_date_filter and end_date_filter:
        return queryset.filter(date__range=(start_date_filter, end_date_filter))
    elif start_date_filter and not end_date_filter:
        return queryset.filter(date__gte=start_date_filter)
    elif not start_date_filter and end_date_filter:
        return queryset.filter(date__lte=end_date_filter)
    else:
        return queryset


def update_sum_of_order(order_id):
    order = Order.objects.get(id=order_id)
    work_in_orders = order.workinorders_set.all()
    total_price = 0
    for i in work_in_orders:
        total_price += i.price * i.amount
    order.total_price = total_price
    order.save()


def form_report_of_patients(report, orders, only_not_paid):
    for order in orders:
        if only_not_paid:
            if order.is_paid:
                continue
        print(order)
        print(order.total_price)
        report['total'] += order.total_price
        report['patients'].append({'patient': order.patient, 'total': 0, 'works': []})
        patient_report = report['patients'][-1]
        work_report = patient_report['works']
        work_in_order = order.workinorders_set.all()
        if work_in_order:
            for work in work_in_order:
                work_report.append(
                    {'work': work.work.work_name, 'price': work.price, 'amount': work.amount})
                patient_report['total'] += work.price * work.amount


def form_report_for_technician(report, technician, operations_query):
    report.append({"technician_name": technician.technician_name, "operations": [], "total": 0})
    operations_report = report[-1]
    for operation in operations_query:
        operation_info = {"operation": operation.operation.operation_name, "price": operation.price,
                          "amount": operation.amount, "total": operation.price * operation.amount}
        operations_report['operations'].append(operation_info)
        report[-1]['total'] += operation_info['total']


class CreateListModelMixin(object):
    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)


class DoctorView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer

    def get_queryset(self):
        """
        doctors only for authenticated owner
        """
        return Doctor.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClinicView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ClinicSerializer

    def get_queryset(self):
        return Clinic.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MaterialView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MaterialSerializer

    def get_queryset(self):
        return Material.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MaterialsOnStockView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MaterialsOnStockSerializer

    def get_queryset(self):
        return MaterialsOnStock.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkSerializer

    def get_queryset(self):
        return Work.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OperationView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OperationSerializer

    def get_queryset(self):
        return Operation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TechnicianView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TechnicianSerializer

    def get_queryset(self):
        return Technician.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MaterialUsedOnOperationView(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MaterialUsedOnOperationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return MaterialUsedOnOperation.objects.filter(user=self.request.user)


class OrderView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkInOrdersView(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkInOrderSerializer

    def get_queryset(self):
        return WorkInOrders.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        update_sum_of_order(serializer.data['order'])

    def perform_update(self, serializer):
        order_replaced = self.get_object().order
        serializer.save()
        update_sum_of_order(serializer.data['order'])
        if order_replaced != serializer.data['order']:
            update_sum_of_order(order_replaced.id)

    def perform_destroy(self, instance):
        instance.delete()
        update_sum_of_order(instance.order.id)


class OperationsInOrdersView(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OperationInOrderSerializer

    def get_queryset(self):
        return OperationsInOrders.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorksPriceListView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorksPriceListSerializer

    def get_queryset(self):
        return WorksPriceList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkPriceView(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkPriceSerializer

    def get_queryset(self):
        return WorkPrice.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OperationsPriceListView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OperationsPriceListSerializer

    def get_queryset(self):
        return OperationsPriceList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OperationPriceView(CreateListModelMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OperationPriceSerializer

    def get_queryset(self):
        return OperationPrice.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorksReportView(views.APIView):
    """
    params:
    doctor - pk, get orders of this doctor (optional)
    clinic - pk, get orders of this clinic (optional)
    start - date %d.%m.%Y, get orders from this date (optional)
    end - date %d.%m.%Y, get order before this date (optional)
    only_not_paid - int, if 1 - shows only not paid works, if 0 - show all works (optional)
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        report = []
        query_params = request.query_params
        clinic_filter, doctor_filter = query_params.get('clinic'), query_params.get('doctor')
        only_not_paid_filter = query_params.get('only_not_paid')

        # Проверяем на целое число
        if clinic_filter:
            clinic_filter = check_is_int(clinic_filter, 'Clinic')
            clinic = Clinic.objects.filter(user=user).filter(id=clinic_filter).first()
            if not clinic:
                raise NotFound(detail='No such clinic')
        if doctor_filter:
            doctor_filter = check_is_int(doctor_filter, 'Doctor')
            doctor = Doctor.objects.filter(user=user).filter(id=doctor_filter).first()
            if not doctor:
                raise NotFound(detail='No such doctor')
        start_date_filter, end_date_filter = [convert_to_datetime(query_params.get('start')),
                                              convert_to_datetime(query_params.get('end'))]
        if only_not_paid_filter:
            only_not_paid_filter = check_is_int(only_not_paid_filter, 'Only Not Paid')

        # Если не заданы клиника и доктор
        if not clinic_filter and not doctor_filter:
            clinics_query, doctors_query = Clinic.objects.filter(user=user), Doctor.objects.filter(user=user)
            orders_query = filter_by_date(Order.objects.filter(user=user), start_date_filter, end_date_filter)
            for clinic in clinics_query:
                orders = orders_query.filter(clinic=clinic).order_by('date')
                report.append({'clinic': clinic.clinic_name, 'total': 0, 'patients': []})
                form_report_of_patients(report[-1], orders, only_not_paid_filter)
            for doctor in doctors_query:
                orders = orders_query.filter(doctor=doctor).filter(clinic=None).order_by('date')
                report.append({'doctor': doctor.doctor_name, 'total': 0, 'patients': []})
                form_report_of_patients(report[-1], orders, only_not_paid_filter)

        # Если задана и клиника, и доктор
        elif doctor_filter and clinic_filter:
            orders_query = filter_by_date(
                Order.objects.filter(user=user).filter(clinic=clinic).filter(doctor=doctor).order_by('date'),
                start_date_filter, end_date_filter)
            report.append({'clinic': clinic.clinic_name, 'doctor': doctor.doctor_name, 'total': 0, 'patients': []})
            form_report_of_patients(report[-1], orders_query, only_not_paid_filter)

        # Если задан только доктор
        elif doctor_filter:
            orders_query = filter_by_date(
                Order.objects.filter(user=user, doctor=doctor).order_by('date'),
                start_date_filter, end_date_filter)
            report.append({'doctor': doctor.doctor_name, 'total': 0, 'patients': []})
            form_report_of_patients(report[-1], orders_query, only_not_paid_filter)

        # Если задана только клиника
        elif clinic_filter:
            orders_query = filter_by_date(
                Order.objects.filter(user=user, clinic=clinic).order_by('date'),
                start_date_filter, end_date_filter)
            report.append({'clinic': clinic.clinic_name, 'total': 0, 'patients': []})
            form_report_of_patients(report[-1], orders_query, only_not_paid_filter)

        # Выводим результат
        return Response(report)


class OperationsReportView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        report = []
        query_params = request.query_params
        start_date_filter, end_date_filter = [convert_to_datetime(query_params.get('start')),
                                              convert_to_datetime(query_params.get('end'))]
        technician_filter = query_params.get('technician')
        if technician_filter:
            technician_filter = check_is_int(technician_filter, 'Technician')
            technician = Technician.objects.filter(user=user).filter(id=technician_filter).first()
            if not technician:
                raise NotFound(detail='No such technician')

            operations_query = filter_by_date(
                OperationsInOrders.objects.filter(user=user).filter(technician=technician).order_by(
                    'date'), start_date_filter, end_date_filter)
            form_report_for_technician(report, technician, operations_query)
        else:
            operations_query = filter_by_date(OperationsInOrders.objects.filter(user=user).order_by('date'),
                                              start_date_filter,
                                              end_date_filter)
            technicians_query = Technician.objects.filter(user=user)
            for technician in technicians_query:
                form_report_for_technician(report, technician, operations_query.filter(technician=technician))
        return Response(report)
