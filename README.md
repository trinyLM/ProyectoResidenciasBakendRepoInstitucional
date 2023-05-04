# ProyectoResidenciasBakendRepoInstitucional
proyecto de residencias profesionales de sistema backend de consulta y adminstración de tesis y reportes de residencias profesionales


---para desplegar este proyecto se reocomienda el deploy en un SO como ubuntu Server o Debian


---instalacion de paquetes necesarios en el servidor
para instalar los paquetes ejecute los siguientes comandos para actualizar
~~~
sudo apt update
sudo apt upgrade
~~~

instalar los paquetes de Python, pip, git y apache

~~~
sudo apt install python3.10.7
sudo apt install build-essential libssl-dev libffi-dev python-dev libpq-dev
apt install python3-pip
sudo apt install git
sudo apt install apache2
~~~


Para verificar que ya tenemos nuestro server corriendo, en nuestro navegador introducimos la IP de nuestro server y nos debería llevar a una página similar a esta:

![](https://help.nextcloud.com/uploads/default/original/2X/1/1c46cfc954ab87f32bbcec2e6bf73d2f12b07964.png)


Lo siguiente es instalar PostgreSQL.
~~~
sudo apt install postgresql postgresql-contrib
~~~

Al instalar PostgreSQL, nos crea un usuario de administración que es el que usaremos para crear nuestro propio usuario, así que lanzamos el siguiente comando para crearlo:

~~~
sudo -u postgres createuser --interactive
~~~

Nos preguntará si queremos que el nuevo usuario sea super usuario y le decimos que si.

Ahora vamos a añadir un password a nuestro usuario, para ello entraremos en la consola de PostgreSQL:

~~~
sudo -u postgres psql
~~~
Y con la siguiente línea añadiremos el password:

~~~
alter user <mi-usuario> with password '<mi-contraseña>';
~~~
Si todo ha salido bien nos retornará ALTER ROLE.

Una vez hecho esto y sin salir de la consola de PostgreSQL, crearemos la base de datos con el siguiente comando.
~~~
CREATE DATABASE <nombre-bbdd>
    WITH 
    OWNER = <mi-usuario>
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
~~~
Y le damos todos los privilegios a nuestro usuario para tener control de la base de datos.
~~~
GRANT ALL PRIVILEGES ON DATABASE <nombre-bbdd> TO <mi-usuario>;
~~~
Y listo, ya tenemos configurada la base de datos, así que solo nos queda salir de la consola de PostgreSQL con el comando \q


el siguiente paso es asegurarnos de que la carpeta /var/www/html pertenezca al grupo de usuarios www-data, este es el grupo que crea apache al instalarlo y la carpeta /var/www/html es el directorio por defecto para desplegar un proyecto con apache.
~~~
sudo chgrp www-data /var/www/html
~~~
Después añadiremos a nuestro usuario al grupo de www-data
~~~
sudo usermod -a -G www-data <mi-usuario>
~~~

Después modificamos los permisos para poder trabajar con el directorio html:
~~~
sudo chmod -R 775 /var/www/html
sudo chmod -R g+s /var/www/html
~~~
Por último nos aseguramos de que nuestro usuario sea el dueño del directorio, esto lo haremos con el siguiente comando:
~~~
sudo chown -R <mi-usuario> /var/www/html
~~~

nos ubicamos dentro de la carpeta var/www/html con el siguiente comando
~~~
cd /var/www/html
~~~
clonnar el codigo fuente del siguiente link con el comando
~~~
git clone https://github.com/trinyLM/ProyectoResidenciasBakendRepoInstitucional.git
~~~


crear nuestro entorno virtual así que lo primero que haremos será instalar la librería para crear los entornos virtuales si no dispone de ella nuestra máquina:
~~~
sudo pip3 install virtualenv 
~~~
Después vamos al directorio de nuestro proyecto,

~~~
cd /var/www/html/ProyectoResidenciasBakendRepoInstitucional
~~~


creamos el entorno virtual y lo activamos:
~~~
virtualenv -p python3 env
source env/bin/activate
~~~
instalamos las librerías que requiera nuestro proyecto.
~~~
pip install -r requirements.txt
~~~
Con pip freeze podremos confirmar que se han instalado nuestras librerías:
~~~
pip freeze
~~~
una vez que tengamos todas las librerias instaladas modificamos el archivo settings.py para que nuestro proyecto funcione este archivo de encunatra en la carpeta repositorioITSZ

~~~
cd repositorioITSZ
~~~
al final del archivo agrega el siguiente codigo y reemplaza name por el nombre de la base de datos que creaste, el usuario y la contraseña por lo que pusiste cudo creaste la base de datos 
~~~
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'repositoriobackend',
        'USER': 'adminrepositorio',
        'PASSWORD':'zongolica2022',
        'HOST': 'localhost',
        'PORT': '5432',
    }
} 
~~~

Posteriormente al final del archivo settings.py agrega el siguiente bloque de codigo, remplazando el email por el proporcionado para uso esclusivo del repositorio institucional y su respectiva contraseña
~~~
EMAIL_FROM = 'trinylm3@gmail.com'#email
EMAIL_BCC = 'trinylm3@gmail.com'#email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'trinylm3@gmail.com'#email
EMAIL_HOST_PASSWORD = 'pukpyzygawmjzayn'
EMAIL_PORT = 587#definir el puerto
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False 

~~~
Añadir el siguiente codigo en el mismo archivo settings.py sustituyendo por la direccion donde se desplegara el proyecto
~~~
CORS_ALLOWED_ORIGINS = ['http://repositorioitsz.sytes.net']
CSRF_TRUSTED_ORIGINS = ['http://repositorioitsz.sytes.net']
~~~

el la terminanal hacemos el collectstatic que nos las descargará en el directorio static/tmp/ dentro de nuestro proyecto.
~~~
python manage.py collectstatic
~~~~
El problema de esto es que si están en un directorio que no es el raíz de static no se muestran y si ya tienes contenido en esa carpeta, como yo que tengo todos los archivos estáticos, los elimina si dices que sí, así que yo hice este apaño del tmp. Lo que haremos después del static es mover el contenido de tmp a static y listo.
~~~
cp -r tmp/* /var/www/html/ProyectoResidenciasBakendRepoInstitucional/static/
rm -R tmp/
~~~

configurar el virtual host, para ello vamos a la siguiente ruta 
~~~
/etc/apache2/sites-available/
~~~
 y creamos el archivo repos.conf (puedes llamarlo como guste).

~~~
sudo nano repo.conf
~~~
Y añadimos el siguiente código:
~~~
<VirtualHost *:80>
    ServerAdmin simple_blog@blog.com
    DocumentRoot /var/www/html/simple_blog
    Alias /static/ /var/www/html/ProyectoResidenciasBakendRepoInstitucional/static/
    Alias /media/  /var/www/html/ProyectoResidenciasBakendRepoInstitucional/media/
    WSGIPassAuthorization On
    WSGIScriptAlias / /var/www/html/ProyectoResidenciasBakendRepoInstitucional/repositorioITSZ/wsgi.py
    WSGIDaemonProcess ProyectoResidenciasBakendRepoInstitucional python-path=/var/www/htmlProyectoResidenciasBakendRepoInstitucional:/var/www/html/ProyectoResidenciasBakendRepoInstitucional/env/lib/python3.10/site-packages
    WSGIProcessGroup simple_blog
</VirtualHost>
~~~
ServerAdmin, es el email que aparecerá cuando nuestra web muestre algún error.
DocumentRoot, ruta de nuestro proyecto.
Alias /static/ y /media/, cuando se intente acceder a esa ruta el servidor tomará la ruta absoluta dada.

WSGIPassAuthorization On, Activa el módulo WSGI.
WSGIScriptAlias / /var/www/html/ProyectoResidenciasBakendRepoInstitucional/repositorioITSZ/wsgi.py, alias del archivo de configuración wsgi.py, todos los proyectos de Django lo tienen.
WSGIDaemonProcess simple_blog python-path=/var/www/html/ProyectoResidenciasBakendRepoInstitucional:/var/www/html/ProyectoResidenciasBakendRepoInstitucional/env/lib/python3.10/site-packages, las librerías del proyecto.
WSGIProcessGroup simple_blog, el nombre que le daremos al proceso.

Antes de continuar tenemos que instalar el módulo WSGIpara Python3 en apache y lo activamos.

~~~
sudo apt-get install libapache2-mod-wsgi-py3
sudo a2enmod wsgi
~~~
Después habilitamos nuestro site recién creado:
~~~
sudo a2ensite repo.conf
~~~
Y reiniciamos apache.
~~~
sudo service apache2 restart
~~~

































