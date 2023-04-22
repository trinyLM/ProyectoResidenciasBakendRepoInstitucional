from pathlib import Path
import os
#from decouple import config




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take configironment variables from .config file

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config('SECRET_KEY')
SECRET_KEY='django-insecure-$te!!n)yfa%$*^b7byf$3%_)4scf_@4o8&whn1^obh2c&_-nv#'
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

#ALLOWED_HOSTS = config('ALLOWED_HOSTS',cast=list) 
ALLOWED_HOSTS=['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #mis aplicaciones
    "autenticacion",
    "archivos",
    "gestion_archivos",

    #django rest framework
    'rest_framework',
    #aplicacion para importar y exportar archivos de excel
    'import_export',
    
    #drf filters
    'django_filters',

    #drf auth token
    'rest_framework.authtoken',
    'authemail',
    #cors
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = 'repositorioITSZ.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'repositorioITSZ.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases




##configurar una ves que se desplego en produccion
""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'repositoriobackend',
        'USER': 'adminrepositorio',
        'PASSWORD':'zongolica2022',
        'HOST': 'localhost',
        'PORT': '5432',
    }
} """

#base de datos provicional 
# se deb de eliminar cuando se despliegue en produccion
""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} """


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
REST_FRAMEWORK = {
    #realizar filtros en las peticiones get
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    
    #sistema de autenticacion por token
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    
    
    #custom docs
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    
    # paginacion default de rest
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 8,
    
}
AUTH_USER_MODEL = "autenticacion.CustomUser"

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_ROOT = os.path.join(BASE_DIR, 'static/tmp/')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# media root
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#campos para el registro con email
#cambiar los valores para el correo institucional 
""" EMAIL_FROM = 'trinylm3@gmail.com'#email
EMAIL_BCC = 'trinylm3@gmail.com'#email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'trinylm3@gmail.com'#email
EMAIL_HOST_PASSWORD = 'pukpyzygawmjzayn'
EMAIL_PORT = 587#definir el puerto
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False """



#settings from corsheaders
CORS_ORIGIN_ALLOW_ALL = True

#modificar y poner la direccion dns
""" CORS_ALLOWED_ORIGINS = ['http://repositorioitsz.sytes.net']
CSRF_TRUSTED_ORIGINS = ['http://repositorioitsz.sytes.net']
 """