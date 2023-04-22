from rest_framework import serializers
from .models import Archivo,Autor,Campus,Carrera,TipoDePublicacion


class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields ="__all__"
    def to_representation(self, instance):
        change = super().to_representation(instance)
        id_tipo_publicacion = change["tipo_de_publicacion"]
        change["tipo_de_publicacion"] = str(
            TipoDePublicacion.objects.get(pk=id_tipo_publicacion))

        lista_de_autores_by_id = change["autor"]
        lista_autores_nombre = []
        for i in lista_de_autores_by_id:
            query = Autor.objects.get(id=i)
            lista_autores_nombre.append(query.nombres)
            change["autor"] = lista_autores_nombre
        return change






class AutorSerializer(serializers.ModelSerializer):
    archivos= serializers.StringRelatedField(many= True)

    
    class Meta:
        model = Autor
        fields = "__all__"
    def to_representation(self,instance):
        changes = super().to_representation(instance)
        id_carrera = changes["carrera"]
        buscar_nombre_carrera = Carrera.objects.get(id=id_carrera)
        changes["carrera"] = buscar_nombre_carrera.nombre

        id_campus = changes["campus"]
        buscar_nombre_campus = Campus.objects.get(id=id_campus)
        changes["campus"] = buscar_nombre_campus.nombre
        return changes 
  
