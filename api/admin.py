from django.contrib import admin
from .models import Administrador, Inspector, Analista, Cliente
admin.site.register(Administrador)
admin.site.register(Inspector)
admin.site.register(Analista)
admin.site.register(Cliente)