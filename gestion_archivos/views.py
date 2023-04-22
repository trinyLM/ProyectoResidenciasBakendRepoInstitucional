from rest_framework import filters
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.response import Response
from archivos.models import Archivo, Autor,Campus,Carrera,TipoDePublicacion
from archivos.pagination import CustomPagination
from archivos.serializers import ArchivoSerializer, AutorSerializer

from .serializers import AutorSimpleSerializer,CampusSimpleSerializer,CarreraSimpleSerializer,TipoDePublicacionSimpleSerializer




class ArchivoCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer


class ArchivoUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer


class ArchivoDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer







class AutorCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutorUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutorDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

"""clases simples para que el administrador genere un select en en front end"""
class AutorSimpleList(viewsets.ViewSet):
    def list(self, request):
        queryset = Autor.objects.all()
        serializer = AutorSimpleSerializer(queryset, many=True)
        return Response(serializer.data)
class CampusSimpleList(viewsets.ViewSet):
    def list(self, request):
        queryset = Campus.objects.all()
        serializer = CampusSimpleSerializer(queryset, many=True)
        return Response(serializer.data)
class CarreraSimpleList(viewsets.ViewSet):
    def list(self, request):
        queryset =Carrera.objects.all()
        serializer = CarreraSimpleSerializer(queryset, many=True)
        return Response(serializer.data)
class TipoDePublicacionSimpleList(viewsets.ViewSet):
    def list(self, request):
        queryset = TipoDePublicacion.objects.all()
        serializer = TipoDePublicacionSimpleSerializer(queryset, many=True)
        return Response(serializer.data)
