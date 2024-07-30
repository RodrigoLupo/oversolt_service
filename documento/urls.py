# documento/urls.py

from django.urls import path
from .views import EmpresaListCreateView, AreaListCreateView, EquipoListCreateView, FajaListCreateView, PoleasListCreateView, ProcesoInspeccionListCreateView, DocumentosListCreateView, ImagenesListCreateView, PoleasProcesoListCreateView, FajasProcesoListCreateView, ParametrosListCreateView, MedicionesListCreateView, TablaListCreateView, FilaListCreateView, ColumnaListCreateView, DatoListCreateView


urlpatterns = [
    path('empresas/', EmpresaListCreateView.as_view(), name='empresa-list-create'),
    path('areas/', AreaListCreateView.as_view(), name='area-list-create'),
    path('equipos/', EquipoListCreateView.as_view(), name='equipo-list-create'),
    path('fajas/', FajaListCreateView.as_view(), name='faja-list-create'),
    path('poleas/', PoleasListCreateView.as_view(), name='poleas-list-create'),
    path('procesos/', ProcesoInspeccionListCreateView.as_view(), name='proceso-list-create'),
    path('documentos/', DocumentosListCreateView.as_view(), name='documentos-list-create'),
    path('imagenes/', ImagenesListCreateView.as_view(), name='imagenes-list-create'),
    path('poleasproceso/', PoleasProcesoListCreateView.as_view(), name='poleasproceso-list-create'),
    path('fajasproceso/', FajasProcesoListCreateView.as_view(), name='fajasproceso-list-create'),
    path('parametros/', ParametrosListCreateView.as_view(), name='parametros-list-create'),
    path('mediciones/', MedicionesListCreateView.as_view(), name='mediciones-list-create'),
    path('tablas/', TablaListCreateView.as_view(), name='tabla-list-create'),
    path('filas/', FilaListCreateView.as_view(), name='fila-list-create'),
    path('columnas/', ColumnaListCreateView.as_view(), name='columna-list-create'),
    path('datos/', DatoListCreateView.as_view(), name='dato-list-create'),
]
