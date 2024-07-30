from django.db import models
from django.contrib.auth.models import User
from api.models import Inspector, Analista, Empresa

class Area(models.Model):
    nombre = models.CharField(max_length=45, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.CharField(max_length=45, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Faja(models.Model):
    estado = models.CharField(max_length=45, null=True, blank=True)
    nPoleas = models.CharField(max_length=45, null=True, blank=True)
    codigo = models.CharField(max_length=45, null=True, blank=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo

class Poleas(models.Model):
    codigo = models.CharField(max_length=45, null=True, blank=True)
    faja = models.ForeignKey(Faja, on_delete=models.CASCADE)
    estado = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.codigo

class ProcesoInspeccion(models.Model):
    procedimiento = models.CharField(max_length=45, null=True, blank=True)
    material = models.CharField(max_length=45, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)

    def __str__(self):
        fajas_nombres = [faja_proceso.faja.codigo for faja_proceso in self.fajasproceso_set.all()]
        poleas_nombres = [polea_proceso.polea.codigo for polea_proceso in self.poleasproceso_set.all()]
        asociados = ', '.join(fajas_nombres + poleas_nombres)

        dato = self.obtener_dato_primer_fila_columna()

        return f"Proceso: {self.procedimiento} ({self.fecha}) - Asociados: {asociados} - Dato: {dato}"

    def obtener_dato_primer_fila_columna(self):
        try:
            tabla = self.parametros_set.first().mediciones_set.first().tabla_set.first()
            if tabla:
                fila = tabla.filas_set.first()
                columna = tabla.columnas_set.first()
                if fila and columna:
                    dato = Dato.objects.filter(fila=fila, columna=columna).first()
                    if dato:
                        return dato.dato
        except AttributeError:
            pass
        return "No data"

class Documentos(models.Model):
    fecha = models.DateField()
    analista = models.ForeignKey(Analista, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=45, null=True, blank=True)
    proceso = models.ForeignKey(ProcesoInspeccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Documento: {self.ubicacion} ({self.fecha})"

class Imagenes(models.Model):
    documento = models.ForeignKey(Documentos, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.ubicacion

class PoleasProceso(models.Model):
    proceso = models.ForeignKey(ProcesoInspeccion, on_delete=models.CASCADE)
    polea = models.ForeignKey(Poleas, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.polea.codigo} - {self.proceso.procedimiento}"

class FajasProceso(models.Model):
    faja = models.ForeignKey(Faja, on_delete=models.CASCADE)
    proceso = models.ForeignKey(ProcesoInspeccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.faja.codigo} - {self.proceso.procedimiento}"

class Parametros(models.Model):
    marca = models.CharField(max_length=45, null=True, blank=True)
    tipo_haz = models.CharField(max_length=45, null=True, blank=True)
    frecuencia = models.CharField(max_length=45, null=True, blank=True)
    ancho_banda = models.CharField(max_length=45, null=True, blank=True)
    amortiguamiento = models.CharField(max_length=45, null=True, blank=True)
    modelo = models.CharField(max_length=45, null=True, blank=True)
    ganancia = models.CharField(max_length=45, null=True, blank=True)
    velocidad = models.CharField(max_length=45, null=True, blank=True)
    retardo = models.CharField(max_length=45, null=True, blank=True)
    diametro = models.CharField(max_length=45, null=True, blank=True)
    proceso = models.ForeignKey(ProcesoInspeccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo

class Mediciones(models.Model):
    tipo = models.CharField(max_length=45, null=True, blank=True)
    nombre = models.CharField(max_length=45, null=True, blank=True)
    parametro = models.ForeignKey(Parametros, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Tabla(models.Model):
    nfilas = models.IntegerField(null=True, blank=True)
    ncol = models.IntegerField(null=True, blank=True)
    medicion = models.ForeignKey(Mediciones, on_delete=models.CASCADE)

    def __str__(self):
        return f"Tabla: {self.medicion} ({self.nfilas}x{self.ncol})"

class Fila(models.Model):
    nombre = models.CharField(max_length=45, null=True, blank=True)
    tabla = models.ForeignKey(Tabla, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Columna(models.Model):
    nombre = models.CharField(max_length=45, null=True, blank=True)
    tabla = models.ForeignKey(Tabla, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Dato(models.Model):
    columna = models.ForeignKey(Columna, on_delete=models.CASCADE)
    fila = models.ForeignKey(Fila, on_delete=models.CASCADE)
    dato = models.CharField(max_length=45, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    inspector = models.ForeignKey(Inspector, on_delete= models.CASCADE )

    def __str__(self):
        return self.dato
