from rest_framework import viewsets
from .serializers import CornerImageSerializer
from ..models import CornerImage

class CornerImageViewSet(viewsets.ModelViewSet):
    queryset = CornerImage.objects.all().order_by('-uploaded')
    serializer_class = CornerImageSerializer