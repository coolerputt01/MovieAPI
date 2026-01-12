from rest_framework import serializers
from .models import FilmModel
from comments.serializers import CommentSerializer

# Film Serilaizer.
class FilmSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = FilmModel
        fields = [
            "id","swapiFilm_id","film_title","release_date","comment_count"
        ]