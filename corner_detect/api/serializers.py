from ..models import CornerImage
from rest_framework import serializers

class CornerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CornerImage
        fields = '__all__'