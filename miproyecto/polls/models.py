import datetime 

from django.db import models  # Importa el módulo models de django.db, necesario para definir modelos

from django.utils import timezone

# Define el modelo Question (Pregunta)
class Question(models.Model):
    # Campo de tipo CharField, que es una clase para almacenar cadenas de texto, con un máximo de 200 caracteres
    question_text = models.CharField(max_length=200)
    # Campo de tipo DateTimeField, que es una clase para almacenar fecha y hora, con una etiqueta "date published"
    pub_date = models.DateTimeField("date published")

    # Método opcional para devolver una representación legible del objeto
    def __str__(self):
        return self.question_text  # Devuelve el texto de la pregunta
      
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Define el modelo Choice (Opción)
class Choice(models.Model):
    # Campo que crea una relación muchos-a-uno con el modelo Question
    # on_delete=models.CASCADE significa que si se elimina la pregunta, también se eliminarán las opciones asociadas
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Campo de tipo CharField para almacenar el texto de la opción, con un máximo de 200 caracteres
    choice_text = models.CharField(max_length=200)
    # Campo de tipo IntegerField para almacenar el número de votos que ha recibido esta opción, con un valor predeterminado de 0
    votes = models.IntegerField(default=0)

    # Método opcional para devolver una representación legible del objeto
    def __str__(self):
        return self.choice_text  # Devuelve el texto de la opción