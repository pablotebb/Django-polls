## PASOS:

1.  Tenemos instalado Django?

    > py -m django --version

    (Mirar FAQs, si quieres instalar Django desde una virtualización)

    [FAQs](../Faq.md)

2.  Creamos un proyecto

    > django-admin startproject myproject

3.  Cambiamos al directorio externo "myproject", y lanzamos el servidor:

    > py manage.py runserver

4.  Creamos la aplicación "polls":

    > py manage.py startapp polls

5.  Creamos la primera vista en **polls/views**

    ```python
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")
    ```

6.  Creamos este código en este otro archivo **polls/urls.py**

    ```python
    from django.urls import path

    from . import views

    urlpatterns = [
        path("", views.index, name="index"),
    ]
    ```

7.  En **myproject/urls.py**:

    ```python
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
      path("polls/", include("polls.urls")),
      path("admin/", admin.site.urls),
    ]
    ```
