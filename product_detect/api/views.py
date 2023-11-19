from rest_framework import viewsets
from .serializers import ProductImageSerializer
from ..models import ProductImage

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all().order_by('-uploaded')
    serializer_class = ProductImageSerializer