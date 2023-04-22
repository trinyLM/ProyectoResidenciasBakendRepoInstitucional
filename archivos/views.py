from rest_framework import filters
from rest_framework import generics
from .models import Archivo, Autor
from .serializers import ArchivoSerializer, AutorSerializer
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class ArchivoList(generics.ListAPIView):
    """Vista que lista todos los archivos, incluye filtro por busqueda general y busqueda especifica"""
    permission_classes = [IsAuthenticated]
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['titulo', 'materia', 'autor__nombres',
                     'tipo_de_publicacion__nombre', 'fecha_publicacion', 'resumen']
    filterset_fields = ['titulo', 'materia', 'fecha_publicacion',
                        'tipo_de_publicacion', "resumen", "autor"]


class ArchivoListDetail(generics.RetrieveAPIView):
    """Muestra una archivo especifico mediante el id"""
    permission_classes = [IsAuthenticated]
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer


class AutorList(generics.ListAPIView):
    """Lista todos los autores existentes, incluye filtro por busqueda general y busqueda especifica"""
    permission_classes = [IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nombres', 'apellido_paterno', 'apellido_materno', 'matricula',
                     'asesor_interno', 'asesor_externo', 'carrera__nombre', 'campus__nombre']
    filterset_fields = ['nombres', 'apellido_paterno', 'apellido_materno',
                        'matricula', 'asesor_interno', 'asesor_externo', 'carrera', 'campus']


class AutorListDetail(generics.RetrieveAPIView):
    """Muestra una autor especifico mediante el id"""
    permission_classes = [IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
