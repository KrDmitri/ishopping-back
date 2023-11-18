from .views import CornerImageViewSet
from rest_framework import routers
from django.urls import path, include

app_name = 'api-corners'

router = routers.DefaultRouter()
router.register(r'corner_detect', CornerImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
