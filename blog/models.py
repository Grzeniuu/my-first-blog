from django.db import models
from django.utils import timezone

#definicja modelu/objektu
#models.Model oznacza że nasz obiekt Post jest modelem Django
#W ten sposób Django wie że powinien go przechowywać w bazie danych
class Post(models.Model):
    #odnośnik do innego modelu
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    #models.CharField - tak definiujemy txt z ograniczną liczbą znakóœ
    title = models.CharField(max_length = 200)
    #models.TextField() to nadaje się do dłuższych tekstów bez ograniczeń
    #ilości znaków. Dla treści wpisu jest ideolo
    text = models.TextField()
    created_date = models.DateTimeField( default = timezone.now)
    published_date = models.DateTimeField( blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
