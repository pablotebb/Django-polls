from django.http import HttpResponse # Importa la clase HttpResponse para enviar respuestas HTTP simples

def index(request):
  # Define la vista index que maneja las solicitudes a una URL específica
  # request: El objeto HttpRequest que contiene datos sobre la solicitud
  return HttpResponse("Hola mundo. Tu estás en el fichero Encuestas.")
  # Retorna una respuesta HTTP con el texto "Hola mundo. Tú estás en el fichero Encuestas."
