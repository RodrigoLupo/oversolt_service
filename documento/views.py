# documento/views.py

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from api.models import Empresa
from .models import  Area, Equipo, Faja, Poleas, ProcesoInspeccion, Documentos, Imagenes, PoleasProceso, FajasProceso, Parametros, Mediciones, Tabla, Fila, Columna, Dato
from .serializers import EmpresaSerializer, AreaSerializer, EquipoSerializer, FajaSerializer, PoleasSerializer, ProcesoInspeccionSerializer, DocumentosSerializer, ImagenesSerializer, PoleasProcesoSerializer, FajasProcesoSerializer, ParametrosSerializer, MedicionesSerializer, TablaSerializer, FilaSerializer, ColumnaSerializer, DatoSerializer

# Empresa CRUD operations
@api_view(['GET', 'POST'])
def empresa_list(request):
    if request.method == 'GET':
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def empresa_detail(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'GET':
        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Area CRUD operations
@api_view(['GET', 'POST'])
def area_list(request):
    if request.method == 'GET':
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def area_detail(request, pk):
    area = get_object_or_404(Area, pk=pk)
    if request.method == 'GET':
        serializer = AreaSerializer(area)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AreaSerializer(area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        area.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Equipo CRUD operations
@api_view(['GET', 'POST'])
def equipo_list(request):
    if request.method == 'GET':
        equipos = Equipo.objects.all()
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EquipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def equipo_detail(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == 'GET':
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EquipoSerializer(equipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        equipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Faja CRUD operations
@api_view(['GET', 'POST'])
def faja_list(request):
    if request.method == 'GET':
        fajas = Faja.objects.all()
        serializer = FajaSerializer(fajas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FajaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def faja_detail(request, pk):
    faja = get_object_or_404(Faja, pk=pk)
    if request.method == 'GET':
        serializer = FajaSerializer(faja)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FajaSerializer(faja, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        faja.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Poleas CRUD operations
@api_view(['GET', 'POST'])
def poleas_list(request):
    if request.method == 'GET':
        poleas = Poleas.objects.all()
        serializer = PoleasSerializer(poleas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PoleasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def poleas_detail(request, pk):
    poleas = get_object_or_404(Poleas, pk=pk)
    if request.method == 'GET':
        serializer = PoleasSerializer(poleas)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PoleasSerializer(poleas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        poleas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ProcesoInspeccion CRUD operations
@api_view(['GET', 'POST'])
def proceso_inspeccion_list(request):
    if request.method == 'GET':
        procesos = ProcesoInspeccion.objects.all()
        serializer = ProcesoInspeccionSerializer(procesos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProcesoInspeccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def proceso_inspeccion_detail(request, pk):
    proceso = get_object_or_404(ProcesoInspeccion, pk=pk)
    if request.method == 'GET':
        serializer = ProcesoInspeccionSerializer(proceso)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProcesoInspeccionSerializer(proceso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        proceso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Documentos CRUD operations
@api_view(['GET', 'POST'])
def documentos_list(request):
    if request.method == 'GET':
        documentos = Documentos.objects.all()
        serializer = DocumentosSerializer(documentos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DocumentosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def documentos_detail(request, pk):
    documento = get_object_or_404(Documentos, pk=pk)
    if request.method == 'GET':
        serializer = DocumentosSerializer(documento)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DocumentosSerializer(documento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        documento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Imagenes CRUD operations
@api_view(['GET', 'POST'])
def imagenes_list(request):
    if request.method == 'GET':
        imagenes = Imagenes.objects.all()
        serializer = ImagenesSerializer(imagenes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ImagenesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def imagenes_detail(request, pk):
    imagen = get_object_or_404(Imagenes, pk=pk)
    if request.method == 'GET':
        serializer = ImagenesSerializer(imagen)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ImagenesSerializer(imagen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        imagen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Parametros CRUD
@api_view(['GET', 'POST'])
def parametros_list(request):
    if request.method == 'GET':
        parametros = Parametros.objects.all()
        serializer = ParametrosSerializer(parametros, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ParametrosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def parametros_detail(request, pk):
    try:
        parametros = Parametros.objects.get(pk=pk)
    except Parametros.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParametrosSerializer(parametros)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ParametrosSerializer(parametros, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        parametros.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Mediciones CRUD
@api_view(['GET', 'POST'])
def mediciones_list(request):
    if request.method == 'GET':
        mediciones = Mediciones.objects.all()
        serializer = MedicionesSerializer(mediciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MedicionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def mediciones_detail(request, pk):
    try:
        mediciones = Mediciones.objects.get(pk=pk)
    except Mediciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MedicionesSerializer(mediciones)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MedicionesSerializer(mediciones, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        mediciones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Tabla CRUD
@api_view(['GET', 'POST'])
def tabla_list(request):
    if request.method == 'GET':
        tabla = Tabla.objects.all()
        serializer = TablaSerializer(tabla, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TablaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tabla_detail(request, pk):
    try:
        tabla = Tabla.objects.get(pk=pk)
    except Tabla.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TablaSerializer(tabla)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TablaSerializer(tabla, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tabla.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Fila CRUD
@api_view(['GET', 'POST'])
def fila_list(request):
    if request.method == 'GET':
        fila = Fila.objects.all()
        serializer = FilaSerializer(fila, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FilaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def fila_detail(request, pk):
    try:
        fila = Fila.objects.get(pk=pk)
    except Fila.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FilaSerializer(fila)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FilaSerializer(fila, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fila.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Columna CRUD
@api_view(['GET', 'POST'])
def columna_list(request):
    if request.method == 'GET':
        columna = Columna.objects.all()
        serializer = ColumnaSerializer(columna, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ColumnaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def columna_detail(request, pk):
    try:
        columna = Columna.objects.get(pk=pk)
    except Columna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ColumnaSerializer(columna)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ColumnaSerializer(columna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        columna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Dato CRUD
@api_view(['GET', 'POST'])
def dato_list(request):
    if request.method == 'GET':
        dato = Dato.objects.all()
        serializer = DatoSerializer(dato, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def dato_detail(request, pk):
    try:
        dato = Dato.objects.get(pk=pk)
    except Dato.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DatoSerializer(dato)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DatoSerializer(dato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)