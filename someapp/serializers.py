from rest_framework.serializers import ModelSerializer
from . import models

class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ['id', 'name', 'country']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'name', 'price', 'manufacturer']