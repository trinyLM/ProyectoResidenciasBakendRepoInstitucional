from django.urls import path
from .views import CampusSimpleList, CarreraSimpleList, TipoDePublicacionSimpleList, AutorSimpleList, ArchivoCreateAPIView, ArchivoUpdateAPIView, ArchivoDeleteAPIView,AutorCreateAPIView, AutorDeleteAPIView, AutorUpdateAPIView
urlpatterns = [

    path("book/create/", ArchivoCreateAPIView.as_view(), name="crear_archivo"),
    path("book/update/<int:pk>", ArchivoUpdateAPIView.as_view(),
         name="actualizar_archivo"),
    path("book/delete/<int:pk>", ArchivoDeleteAPIView.as_view(),
         name="eliminar_archivo"),

    path("autor/create/", AutorCreateAPIView.as_view(), name="crear_Autor"),
    path("autor/update/<int:pk>", AutorUpdateAPIView.as_view(),
         name="actualizar_Autor"),
    path("autor/delete/<int:pk>",
         AutorDeleteAPIView.as_view(), name="eliminar_Autor"),

    # url para consultar una lista simple desde el front end
    path("lista/autores/",
         AutorSimpleList.as_view({'get': 'list'}), name="simplelist_Autor"),
    path("lista/campus/",
         CampusSimpleList.as_view({'get': 'list'}), name="simplelist_Campus"),
    path("lista/carreras/",
         CarreraSimpleList.as_view({'get': 'list'}), name="simplelist_Carrera"),
    path("lista/tiposdepublicacion/",
         TipoDePublicacionSimpleList.as_view({'get': 'list'}), name="simplelist_Tipodepublicacion"),


]
