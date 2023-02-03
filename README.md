# Django

Django corriendo en Ubuntu 22.04. Pasos de todo lo necesario para la instalación, creación de proyecto, etc.

## INSTALACIÓN (DE TODO LO NECESARIO)
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
[sudo] pip3 install django
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

**Si no se ha hecho la instalación con sudo, añadir un directorio a la variable path del sistema (poner al final de este archivo)**
```
gedit ~/.bashrc
```
```
PATH=$PATH:~/.local/bin
export PATH
```

### PYTHON (TODO LO NECESARIO)
Sin root, da igual la carpeta:
```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
sudo apt-get install python3-dev default-libmysqlclient-dev libzstd-dev
pip install mysqlclient
pip install django-extensions
```

--- creacion proyecto:

django-admin startproject mysite

python manage.py runserver (dentro de mysite (1ero))

python manage.py startapp polls (dentro de mysite (1ero))


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


