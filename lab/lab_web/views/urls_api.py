from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()
router.register('doctors', DoctorView, basename='doctor')
router.register('clinics', ClinicView, basename='clinic')
router.register('materials', MaterialView, basename='material')
router.register('materials_on_stock', MaterialsOnStockView, basename='material_on_stock')
router.register('works', WorkView, basename='work')
router.register('operations', OperationView, basename='operation')
router.register('operations_in_work', OperationsInWorkView, basename='operation_in_work')
router.register('technicians', TechnicianView, basename='technician')
router.register('files', FileView, basename='file')
router.register('materials_used_on_operation', MaterialUsedOnOperationView, basename='material_used_on_operation')
router.register('orders', OrderView, basename='order')
router.register('work_in_orders', WorkInOrdersView, basename='work_in_orders')
router.register('operations_in_orders', OperationsInOrdersView, basename='operation_in_orders')
router.register('works_price_lists', WorksPriceListView, basename='works_price_list')
router.register('works_prices', WorkPriceView, basename='works_price')
router.register('operations_price_lists', OperationsPriceListView, basename='operations_price_list')
router.register('operations_prices', OperationPriceView, basename='operations_price')

urlpatterns = router.urls
