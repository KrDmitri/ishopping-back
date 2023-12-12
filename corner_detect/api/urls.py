from .views import CornerImageViewSet
from .views import get_info_view
# from .views import get_data_from_database
from rest_framework import routers
from django.urls import path, include

app_name = 'api-corners'

router = routers.DefaultRouter()
router.register(r'corner_detect', CornerImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get-info/', get_info_view, name='get_info'),
    # path('get-db-data/', get_data_from_database, name='get_db_data'),
]
