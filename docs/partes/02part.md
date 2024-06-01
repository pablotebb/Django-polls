## PASOS:

1. Fijarse en el fichero **myproject/settings.py**

   - Tenemos en DATABASES default, el motor por defecto de "sqlite". Si queremos cambiar a otra BD (PostgreSQL, desde el principio, para que no nos de dolor dé cabeza), mirar [aquí](https://docs.djangoproject.com/es/5.0/intro/tutorial02/)
   - Debemos poner en TIME_ZONE, nuestra zona horaria
   - En INSTALLED_APPS, tenemos todas las aplicaciones que podemos usar en nuestros proyectos.

2. Las aplicaciones (INSTALLED_APPS), usan casi siempre tablas en la BDs, por lo que necesitamos crearlas antes de utilizarlas:

   > py manage.py migrate

3. Editamos **polls/models.p**:

   ```python
   from django.db import models


   class Question(models.Model):
      question_text = models.CharField(max_length=200)
      pub_date = models.DateTimeField("date published")


   class Choice(models.Model):
      question = models.ForeignKey(Question, on_delete=models.CASCADE)
      choice_text = models.CharField(max_length=200)
      votes = models.IntegerField(default=0)
   ```

   > Activando modelos

   > Ese pequeño fragmento de código del modelo le da a Django mucha información. Con él, Django es capaz de:

   - Cree un esquema de base de datos ( declaraciones) para esta aplicación.CREATE TABLE
   - Cree una API de acceso a la base de datos de Python para acceder Question y Choice objetos.

4. Debemos decirle a nuestro proyecto que la aplicación polls está instalada. La clase **PollsConfig** que esta en el archivo **polls/apps.py**, por ello debemos editar el archivo **myproject/settings.py**, y agregar esta ruta en INSTALLED_APPS.

```python
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

5. Ejecutamos migración

   > py manage.py makemigrations polls

   Nota - Las migraciones son la forma en que Django almacena los cambios en sus modelos. Puedes leer la migración para tu nuevo modelo si lo deseas; es el archivo **polls/migrations/0001_initial.py**

6. El comando sqlmigrate toma los nombres de las migraciones y devuelve sql:
   > py manage.py sqlmigrate polls 0001

```python
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```

7. A continución, ejecutamos el comando migrate
   para crear esas tablas modelos en su base de datos:
   > py manage.py migrate

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
```

8. Jugando con la Api

   > py manage.py shell

   ```
      from polls.models import Choice, Question
      ...
   ```

   [Mirar aquí](https://docs.djangoproject.com/en/5.0/intro/tutorial02/)

9. Presentamos el administrador de Django

   > py manage.py createsuperuser

   User: admin
   email:
   password:

   > py manage.py runserver

   > http://127.0.0.1:8000/admin/

   **Hacer que la aplicación de encuesta sea modificable en el administrador**

   - Para hacer esto, abra el **polls/admin.py** archivo y edítelo para que se vea así:

   ```
   from django.contrib import admin

   from .models import Question

   admin.site.register(Question)
   ```

   [Mirar aquí](https://docs.djangoproject.com/en/5.0/intro/tutorial02/)
