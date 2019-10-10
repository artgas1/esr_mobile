from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()
router.register('doctors', DoctorView, basename='doctor')
router.register('clinics', ClinicView, basename='clinic')
router.register('materials', MaterialView, basename='material')
router.register('materials_on_stock', MaterialsOnStockView, basename='materials_on_stock')

urlpatterns = router.urls
