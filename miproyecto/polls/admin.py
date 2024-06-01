from django.contrib import admin  # Importa el módulo admin, que contiene las funcionalidades de administración

from .models import Question  # Importa el modelo Question desde el archivo models.py del mismo directorio

admin.site.register(Question)  # Registra el modelo Question en la interfaz de administración de Django
# Esto permite gestionar el modelo Question (añadir, editar, eliminar) desde la interfaz de administración web
