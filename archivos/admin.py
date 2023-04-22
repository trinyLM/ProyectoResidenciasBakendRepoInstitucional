from django.contrib import admin
from .models import Archivo,Autor,TipoDePublicacion,Carrera,Campus
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin import AdminSite


class ArchivoResource(resources.ModelResource):
    class Meta:
        model = Archivo

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class ArchivoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('titulo','materia','fecha_publicacion',"Autor")
    search_fields=["titulo",'materia',]
    list_filter = ("materia","fecha_publicacion",)
    resource_class=ArchivoResource
    
class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("nombres","apellido_paterno","apellido_materno","matricula","asesor_interno","asesor_externo")
    search_fields=["nombres","apellido_paterno","apellido_materno","matricula","asesor_interno","asesor_externo"]
    list_filter = ("nombres","apellido_paterno","apellido_materno","matricula","asesor_interno","asesor_externo")
    resource_class=AutorResource
    
class TipoDePublicacionAdmin(admin.ModelAdmin):
    list_display=("nombre","descripcion",)
    
    # Register your models here.
admin.site.register(Carrera)
admin.site.register(Autor,AutorAdmin)
admin.site.register(TipoDePublicacion,TipoDePublicacionAdmin)
admin.site.register(Archivo,ArchivoAdmin)
admin.site.register(Campus)



#clase para quitar el tema defecto


admin.site.site_header = "Repositorio ITSZ"
admin.site.site_title = "Administracion del Repositorio"