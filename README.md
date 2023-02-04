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
### Creamos el proyecto 
Comprobamos que funcione, ejecutamos los siguientes comandos y entramos a localhost:8000 en el navegador. Nos tiene que salir el cohete.
```
django-admin startproject mysite
cd mysite
python manage.py runserver (lo ejecutamos al mismo nivel que manage.py)
```
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

```
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
```




python manage.py runserver (dentro de mysite (1ero)) y visitar localhost:8000/polls/

#añadir a la app de encuestas una ruta que sea holamundo para que cuando la visites pinte tu nombre



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