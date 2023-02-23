from django.contrib import admin
from .models import Linea, Estacion, Incidencia

# Register your models here.
# admin.site.register(Linea)
# admin.site.register(Estacion)
# admin.site.register(Incidencia)

class EstacionInline(admin.TabularInline):
    model=Estacion

class LineaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nombre',     {'fields': ['nombre']}),
        ('Color',      {'fields': ['color']}),
        ('Distancia',  {'fields': ['distancia']}),
    ]
    inlines = [EstacionInline]
    list_per_page = 10

admin.site.register(Linea, LineaAdmin)

class IncidenciaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Texto',      {'fields': ['texto']}),
        ('Fecha',      {'fields': ['fecha']}),
    ]
    list_display = ('texto', 'fecha')
    list_filter = ['fecha']
    list_per_page = 10

admin.site.register(Incidencia, IncidenciaAdmin)