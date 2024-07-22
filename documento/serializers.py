from api.models import Empresa
from rest_framework import serializers
from .models import  Area, Equipo, Faja, Poleas, ProcesoInspeccion, Documentos, Imagenes, PoleasProceso, FajasProceso, Parametros, Mediciones, Tabla, Fila, Columna, Dato

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'

class FajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faja
        fields = '__all__'

class PoleasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poleas
        fields = '__all__'

class FajasProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FajasProceso
        fields = '__all__'

class PoleasProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoleasProceso
        fields = '__all__'

class ProcesoInspeccionSerializer(serializers.ModelSerializer):
    faja_id = serializers.IntegerField(write_only=True, required=False)
    polea_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = ProcesoInspeccion
        fields = '__all__'

    def create(self, validated_data):
        faja_id = validated_data.pop('faja_id', None)
        polea_id = validated_data.pop('polea_id', None)

        proceso_inspeccion = ProcesoInspeccion.objects.create(**validated_data)

        if faja_id:
            FajasProceso.objects.create(faja_id=faja_id, proceso=proceso_inspeccion)
        if polea_id:
            PoleasProceso.objects.create(polea_id=polea_id, proceso=proceso_inspeccion)

        return proceso_inspeccion

class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentos
        fields = '__all__'

class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = '__all__'

class ParametrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametros
        fields = '__all__'

class MedicionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mediciones
        fields = '__all__'

class TablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabla
        fields = '__all__'

class FilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fila
        fields = '__all__'

class ColumnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Columna
        fields = '__all__'

class DatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dato
        fields = '__all__'