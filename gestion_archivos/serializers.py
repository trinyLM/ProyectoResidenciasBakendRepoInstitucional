from rest_framework import serializers
from archivos.models import Autor,TipoDePublicacion,Campus,Carrera


class AutorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields ="__all__"

class TipoDePublicacionSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDePublicacion
        fields ="__all__"
class CampusSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields ="__all__"
class CarreraSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields ="__all__"
