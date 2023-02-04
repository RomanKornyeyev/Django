# Django

Django corriendo en Ubuntu 22.04. Pasos de todo lo necesario para la instalación, creación de proyecto, etc.

## ---------------- INSTALACIÓN (DE TODO LO NECESARIO) ----------------
### APT UPDATE (ANTES DE NADA)
```
sudo apt-get update
```
### PIP (GESTOR DE LIBRERÍAS)
```
sudo apt-get install python3-pip
```

### DJANGO
```
pip3 install django
sudo apt install python3-django
```

**cada vez que escribas python, ejecute python3:**
```
sudo apt install python-is-python3
```

**¿Cómo ver la version?**
```
python --version
python -m django --version
```

**Si no se ha hecho la instalación con sudo (recomendado hacerlo sin sudo), añadir un directorio a la variable path del sistema (poner al final de este archivo)**
```
gedit ~/.bashrc
```
```
PATH=$PATH:~/.local/bin
export PATH
```

### PYTHON (TODO LO NECESARIO)
```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
sudo apt-get install python3-dev default-libmysqlclient-dev libzstd-dev
pip install mysqlclient
pip install django-extensions
```

## ---------------- CREACIÓN DEL PROYECTO ----------------
### --- PARTE 1 ---
### Creamos el proyecto 
Comprobamos que funcione, ejecutamos los siguientes comandos y entramos a localhost:8000 en el navegador. Nos tiene que salir el cohete.
```
django-admin startproject mysite
cd mysite
python manage.py runserver (lo ejecutamos al mismo nivel que manage.py)
```
Esto nos dejará el siguiente árbol:
<pre>
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
</pre>
### creamos nuestra primera app
Paramos el server con ctrl+c y ejecutamos este comando:
```
python manage.py startapp polls (lo ejecutamos al mismo nivel que manage.py)
```
**Creamos nuestra primera vista (hola mundo)**
copiamos y pegamos esto en views:
```
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
Para llamar a esta vista, NECESITAMOS MAPEAR ESTO A UNA URL. Creamos un urls.py en polls, con lo que nos queda esta jerarquía:

<pre>
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
</pre>

En este urls.py (dentro de polls), incluímos el siguiente código:

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
Del directorio actual, importame views (vistas). Entonces cuando visites localhost:8000/polls/ vas a ejecutar el index del view. Pero esto no acaba aquí, ahora estas urls hay que incluirlas en las urls generales (mysite/urls.py), nos quedaría el siguiente código:
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
Con include podemos hacer referencia a otras URLS de otros proyectos. Así podemos hacer fácilmente un plug and play de urls. Ahora ejecutamos runserver y entramos en localhost:8000/polls/ y veremos el "hola mundo".
```
python manage.py runserver 
```


### --- PARTE 2 ---
### Configuración de base de datos
Usaremos mariadb como base de datos. Antes de nada, deberemos crear una nueva base de datos en nuestro gestor, accedemos al gestor como root y creamos una base de datos, un usuario y le concedemos privilegios de lectura/escritura al usuario sobre la base de datos. Para ello, ejecutaremos los siguientes comandos:
```
CREATE DATABASE mysite; //NB BASE DE DATOS
CREATE USER 'user_mysite'@'localhost' IDENTIFIED BY '123456'; //NB USUARIO - CONTRASEÑA (IDENTIFIED)
GRANT ALL PRIVILEGES ON mysite.* TO 'user_mysite'@'localhost' WITH GRANT OPTION; //CONCEDER TODOS LOS PRIVILEGIOS AL USUARIO user_mysite SOBRE LA BASE DE DATOS mysite
```







python3 manage.py migrate

en mysql:
use mysite;
show tables;
desc django_session;

python manage.py makemigrations polls
python manage.py migrate polls(sí, otra vez)
#esto crea tablas nuevas en la BD, por tanto hay que tener bien el user y password en settings.py


python manage.py createsuperuser (donde esta el fichero manage.py)
se accede con localhost:8000/admin (en el navegador)