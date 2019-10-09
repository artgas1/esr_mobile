from rest_framework.routers import DefaultRouter
from .api import DoctorView

router = DefaultRouter()
router.register('doctors', DoctorView, basename='doctor')
urlpatterns = router.urls
