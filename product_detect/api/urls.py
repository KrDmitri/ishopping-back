from .views import ProductImageViewSet
from rest_framework import routers
from django.urls import path, include

app_name = 'api-products'

router = routers.DefaultRouter()
router.register(r'product_detect', ProductImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]