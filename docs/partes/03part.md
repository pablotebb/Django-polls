## PASOS:

1. En nuestra aplicación de encuesta, tendremos las siguientes cuatro vistas:

   - Página de “índice” de preguntas: muestra las últimas preguntas.
   - Página de “detalle” de la pregunta: muestra el texto de una pregunta, sin resultados pero con un formulario para votar.
   - Página de “resultados” de la pregunta: muestra los resultados de una pregunta en particular.
   - Acción de voto: maneja la votación por una opción particular en una pregunta particular.

2. En Django, las páginas web y otros contenidos se entregan mediante vistas. Cada vista está representada por una función de Python (o método, en el caso de vistas basadas en clases). Django elegirá una vista examinando la URL solicitada (para ser precisos, la parte de la URL después del nombre de dominio).

3. Para pasar de una URL a una vista, Django utiliza lo que se conoce como **'URLconfs'**. Una URLconf asigna patrones de URL a vistas. <br>
   Ej: `/newsarchive/<year>/<month>/`

4. Escribiendo más vistas

> polls/views.py

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

5. Conectando las vistas al polls.urls

> polls/urls.py

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

6. Resultado en la web

   ```

   http://127.0.0.1:8000/polls/

      Hola mundo. Tu estás en el fichero Encuestas.

   http://127.0.0.1:8000/polls/34/

      You're looking at question 34.

   http://127.0.0.1:8000/polls/34/results/

      You're looking at the results of question 34.

   http://127.0.0.1:8000/polls/34/vote/

      You're voting on question 34.

   ```
