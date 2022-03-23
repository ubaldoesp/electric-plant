from rest_framework import serializers
from .models import Bitacora


class BitacoraSerializer(serializers.ModelSerializer):

    def validate_dispositivo(self, dispositivo):
        if dispositivo.status == 1:
            raise serializers.ValidationError(f"Dispositivo en 'mantenimiento', por favor actualizar a 'operacion'")
        return dispositivo

    class Meta:
        model = Bitacora
        fields = '__all__'
