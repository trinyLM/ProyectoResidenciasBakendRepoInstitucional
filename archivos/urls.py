from django.urls import path
from .views import ArchivoList, ArchivoListDetail,AutorList,AutorListDetail

urlpatterns=[
    path("archivo/",ArchivoList.as_view() ,name="archivos"),
    path("archivo/<int:pk>",ArchivoListDetail.as_view(),name="archivo_detail"),
    path("autor/" ,AutorList.as_view(),name="autor"),
    path("autor/<int:pk>",AutorListDetail.as_view(),name="autor_detail"),
    ]