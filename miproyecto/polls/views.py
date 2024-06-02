from django.http import HttpResponse # Importa la clase HttpResponse para enviar respuestas HTTP simples

def index(request):
  # Define la vista index que maneja las solicitudes a una URL específica
  # request: El objeto HttpRequest que contiene datos sobre la solicitud
  return HttpResponse("Hola mundo. Tu estás en el fichero Encuestas.")
  # Retorna una respuesta HTTP con el texto "Hola mundo. Tú estás en el fichero Encuestas."
  

# Definimos la función detail que toma dos parámetros: request y question_id.
def detail(request, question_id):
    # La función devuelve una respuesta HTTP que contiene una cadena de texto con el ID de la pregunta.
    return HttpResponse("You're looking at question %s." % question_id)

# Definimos la función results que también toma dos parámetros: request y question_id.
def results(request, question_id):
    # Creamos una cadena de texto con un marcador de posición para el ID de la pregunta.
    response = "You're looking at the results of question %s."
    # La función devuelve una respuesta HTTP que contiene la cadena de texto con el ID de la pregunta.
    return HttpResponse(response % question_id)

# Definimos la función vote que toma dos parámetros: request y question_id.
def vote(request, question_id):
    # La función devuelve una respuesta HTTP que contiene una cadena de texto con el ID de la pregunta.
    return HttpResponse("You're voting on question %s." % question_id)

