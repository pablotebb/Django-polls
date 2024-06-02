from django.urls import path  # Importa la función path para definir rutas URL
from . import views # Importa el módulo views desde el paquete actual

# urlpatterns = [
#   # Define una ruta URL para la raíz de la aplicación polls
#   # Llama a la vista index cuando el usuario accede a /polls/
#   path("", views.index, name="index"),
# ]



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