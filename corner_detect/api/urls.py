from .views import CornerImageViewSet
from .views import get_info_view, get_location_view, test_function, get_info_by_barcode, get_info_by_qr
from rest_framework import routers
from django.urls import path, include

# tibero
# from .views import get_data_from_database

app_name = 'api-corners'

router = routers.DefaultRouter()
router.register(r'corner_detect', CornerImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get-info/', get_info_view, name='get_info'),
    path('get-location/', get_location_view, name='get_location'),
    path('test/', test_function, name='test'),
    path('get-info-by-barcode/', get_info_by_barcode, name='get_info_by_barcode'),
    path('get-info-by-qr/', get_info_by_qr, name='get_info_by_qr'),

    # path('get-db-data/', get_data_from_database, name='get_db_data'),
]
