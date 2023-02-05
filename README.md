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
### TIME ZONE
Antes de seguir modificando el settings.py, estableceremos la zona horaria acorde a nuestra zona horaria (genius), en este caso, Madrid.
```
TIME_ZONE = 'Europe/Madrid'
```

### Configuración de base de datos
Usaremos mariadb como base de datos. Antes de nada, deberemos crear una nueva base de datos en nuestro gestor, accedemos al gestor como root y creamos una base de datos, un usuario y le concedemos privilegios de lectura/escritura al usuario sobre la base de datos. Para ello, ejecutaremos los siguientes comandos:
```
CREATE DATABASE mysite; //NB BASE DE DATOS
CREATE USER 'user_mysite'@'localhost' IDENTIFIED BY '123456'; //NB USUARIO - CONTRASEÑA (IDENTIFIED)
GRANT ALL PRIVILEGES ON mysite.* TO 'user_mysite'@'localhost' WITH GRANT OPTION; //CONCEDER TODOS LOS PRIVILEGIOS AL USUARIO user_mysite SOBRE LA BASE DE DATOS mysite
```

Una vez hecho esto, vamos a configurar esto en Django. Nos vamos a mysite/settings.py y nos vamos a la sección de DATABASES. Deberemos meter el siguiente código:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite',
        'USER': 'user_mysite',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

Ahora que hemos realizado cambios en el acceso a la base de datos Y CADA VEZ QUE HAGAMOS CAMBIOS EN LOS MODELOS DE LA BASE DE DATOS. tenemos que hacer una migración, para que Django nos cree las tablas correspondientes en nuestra base de datos:
```
python manage.py migrate
```

**Podemos también migrar únicamente aplicaciones/carpetas en específico (en este caso no es necesario):**
```
python manage.py migrate [polls]
```

Una vez hechas las migraciones, podremos comprobar en nuestra base de datos que se han creado las nuevas tablas de DJango.
```
show tables;
desc django_session;
```

### Creación de modelos
Crearemos los modelos (tablas de BD), nos iremos a polls/models.py y pondremos el siguiente código (este es de ejemplo):
```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Más info sobre modelos: https://docs.djangoproject.com/en/4.1/topics/db/models/ <br>
Bien, con esto ya tendríamos los modelos definidos. **Ahora necesitamos activar estos modelos, incluir esta app en nuestro proyecto (polls en mysite)**. Para ello nos vamos a mysite/settings.py y añadimos al array de INSTALLED_APPS el valor 'polls.apps.PollsConfig', este valor sale de polls/apps.py. Nos quedaría el siguiente código:
```
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Ahora Django sabe que tiene que incluir la app polls. Haremos otro comando (migración):
```
python manage.py makemigrations polls
```

Deberemos ver algo similar a esto:
```
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

Haciendo esto le estás diciendo a Django que has hecho cambios en los modelos (en este caso has creado nuevos). Y que te gustaría guardar esos cambios como una migración.<br>
Volvemos a hacer una migración:
```
python manage.py migrate 
```
```
python manage.py migrate [polls]
```

Esto nos crea las nuevas tablas de los modelos en la base de datos.

### Jugando con la API
Me lo voy a saltar, dejaré solamente unos comandos core:
```
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

Por defecto los objetos nos devuelven "Question object (1)", para modificar esto, símplemente le metemos un "to.String" a los modelos:
```
def __str__(self):
    return self.question_text
```

### Django admin
Antes de nada, tendremos que crear un usuario que administre la aplicación.
```
python manage.py createsuperuser
```

Seguimos los pasos que nos marca el shell, establecemos el nombre, correo y contraseña y listo.<br>
**Ejecutamos el servidor y entramos en localhost:8000/admin en el navegador.**
```
python manage.py runserver
```

Nos logueamos y deberíamos ver el dashboard. Pero... este dashboard no tiene las tablas de los modelos de nuestra aplicación (polls) ¿Cómo las añadimos?

**Haremos que la app polls sea modificable en admin, importando los modelos en el fichero polls/admin.py:**
```
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```

Ahora podremos añadir datos a nuestros modelos/tablas.


### --- PARTE 3 ---

a