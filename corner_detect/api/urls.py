from .views import CornerImageViewSet
from .views import get_info_view
from rest_framework import routers
from django.urls import path, include

app_name = 'api-corners'

router = routers.DefaultRouter()
router.register(r'corner_detect', CornerImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get-info/', get_info_view, name='get_info'),
]
