from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from django.contrib.auth import views as auth_views
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),

    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='admin_password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),





    #urls de la api desarrrollada
    path("api/", include("archivos.urls")),
    path("api/gestion/", include("gestion_archivos.urls")),
    path('api/auth/', include('authemail.urls')),
    path("docs/", include_docs_urls(title='Documentacion API repositorio ITSZ', public=True)),

]
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
