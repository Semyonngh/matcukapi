from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Manufacturer
from .serializers import ManufacturerSerializer

class ManufacturerViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

    @action(detail=False, url_path='russian')
    def russian_manufacturers(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(country__iexact='Russia')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        name = serializer.validated_data['name']
        if not name.startswitch('ООО'):
            name = 'ООО' + name
            serializer.validated_data['name'] = name
        return super().perform_create(serializer)