from django.db import models
from films.models import FilmModel


# Comment Model.
class CommentModel(models.Model):
    film_id = models.ForeignKey(FilmModel,related_name="comments",on_delete=models.CASCADE)
    content = models.CharField(max_length=500,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content} at {self.created_at}"