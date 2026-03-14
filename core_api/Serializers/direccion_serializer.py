from rest_framework import  serializers
from admin_geomike.models import Direccion


class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = ['empleado', 'latitud', 'longitud']