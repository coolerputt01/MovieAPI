from django.db import models


# Film Model
class FilmModel(models.Model):
    swapiFilm_id = models.IntegerField(unique=True,blank=False)
    film_title = models.CharField(max_length=255,blank=False)
    release_date = models.DateField(blank=False)

    def __str__(self):
        return f"{self.film_title} at {self.release_date}"