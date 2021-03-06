from rest_framework import viewsets

from db.api import serializers
from db.base.models import Satellite, Transponder


class SatelliteView(viewsets.ModelViewSet):
    queryset = Satellite.objects.all()
    serializer_class = serializers.SatelliteSerializer


class TransponderView(viewsets.ModelViewSet):
    queryset = Transponder.objects.all()
    serializer_class = serializers.TransponderSerializer
